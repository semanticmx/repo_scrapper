import requests


class BaseAPIService:
    endpoint_url_format = 'https://{hostname}/{version}/{relative_path}'

    def build_endpoint_path(self, relative_path):
        """
        prepares the API URL based on relative_path

        """
        return self.endpoint_url_format.format(relative_path=relative_path)

    def get(self, relative_path, **kwargs):
        """
        Performs a GET request and returns response.

        """
        url = self.build_endpoint_path(relative_path)
        return requests.get(url, **kwargs)


class GitHubAPIService(BaseAPIService):
    """
    GitHub API class

    """
    endpoint_url_format = 'https://api.github.com{relative_path}'
