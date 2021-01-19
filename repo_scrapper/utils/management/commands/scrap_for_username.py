from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from repo_scrapper.api.services.github import GitHubService
from repo_scrapper.core import models as core_models


class Command(BaseCommand):
    help = 'Scrapes github repositories info for given username'
    username = None
    service = GitHubService()
    follower_depth = 0
    following_depth = 0

    def add_arguments(self, parser):
        parser.add_argument('--username', help='github username')

    def _get_json_data(self, endpoint_function, **kwargs):
        """
        returns json data or raises and exception

        """
        if kwargs.get('username') is None:
            kwargs['username'] = self.username

        response = endpoint_function(**kwargs)

        if response.status_code > 299:
            raise CommandError(f'we were not able to connect to {self.username}[{response.status_code}]')

        return response.json()

    def get_data_from_followers(self, username=None):
        """
        gets data from username followers

        """
        if self.follower_depth > settings.MAX_FOLLOWERS_DEPTH:
            self.stdout.write(self.style.NOTICE(f'Max followers depth reached at {username}'))
            return

        self.follower_depth += 1

        data = self._get_json_data(
            endpoint_function=self.service.get_followers,
            username=username
        )
        for repo_info in data:
            follower = repo_info.get('login')
            self.get_data_from_owner(username=follower)
            self.get_data_from_followers(username=follower)

    def get_data_from_owner(self, username=None):
        """
        scrapes info from repo owner

        """
        data = self._get_json_data(
            endpoint_function=self.service.get_user_repos,
            username=username
        )
        for repo_info in data:
            repo = core_models.Repository()
            repo.create_from_json(data=repo_info)
            self.stdout.write(self.style.NOTICE(f'Scrapping {repo}'))

    def get_user_data(self):
        """
        collects repository info for self.username

        """
        self.get_data_from_owner()
        self.get_data_from_followers()
        self.get_data_from_following_users()

    def handle(self, *args, **options):
        self.username = options.get('username')
        if self.username is None:
            raise CommandError('You need to pass a --username')

        self.get_user_data()

        self.stdout.write(self.style.SUCCESS(f'Successfully scrapped data for {self.username}'))
