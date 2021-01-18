from repo_scrapper.api.clients import GitHubAPIService


class GitHubService(GitHubAPIService):
    """
    wrapper around GitHub API

    """
    def get_user_repos(self, username):
        """
        retrieves all public repos info from username

        """
        path = f'/users/{username}/repos'
        return self.get(relative_path=path)

    def get_followers(self, username):
        """
        retrieves followers info

        """
        path = f'/users/{username}/followers'
        return self.get(relative_path=path)

    def get_following(self, username):
        """
        retrieves followers info

        """
        path = f'/users/{username}/following'
        return self.get(relative_path=path)
