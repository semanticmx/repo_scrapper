import logging

from django.db import models
from django.db.utils import IntegrityError

logger = logging.getLogger(__name__)


class User(models.Model):
    github_id = models.IntegerField(unique=True)
    login = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f'{self.login}'


class Repository(models.Model):
    github_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, blank=False)
    full_name = models.CharField(max_length=512)
    html_url = models.URLField()
    git_url = models.URLField()
    language = models.CharField(max_length=255)
    disabled = models.BooleanField(default=False)
    stargazers_count = models.IntegerField(default=0)
    watchers_count = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=False)

    def _load_repo_from_json(self, data):
        """
        loads json data into model fields

        """
        self.github_id = data.get('id')
        self.name = data.get('name')
        self.full_name = data.get('full_name')
        self.html_url = data.get('html_url')
        self.git_url = data.get('git_url')
        self.language = data.get('language')
        self.disabled = data.get('disabled')
        self.stargazers_count = data.get('stargazers_count')
        self.watchers_count = data.get('watchers_count')
        self.forks = data.get('forks')

    def _load_user_from_json(self, data):
        """
        loads json data into User model from repo data

        """
        user = User()
        user.github_id = data.get('id')
        user.login = data.get('login')
        user.url = data.get('url')
        self.owner = user

    def create_from_json(self, data):
        self._load_repo_from_json(data)

        owner = data.get('owner')
        if owner is not None:
            self._load_user_from_json(data=owner)

        try:
            self.owner.save()
            self.save()
        except IntegrityError:
            logger.info(f'Repository {self.git_url} already added.')

    def __str__(self):
        return f'[{self.github_id}] {self.owner.login} {self.git_url}'
