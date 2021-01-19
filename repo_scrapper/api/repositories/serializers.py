from rest_framework import serializers

from repo_scrapper.core import models as core_models
from repo_scrapper.api.users.serializers import GitHubUserSerializer


class RepositorySerializer(serializers.ModelSerializer):
    owner = GitHubUserSerializer()

    class Meta:
        model = core_models.Repository
        fields = [
            'github_id',
            'name',
            'full_name',
            'html_url',
            'git_url',
            'language',
            'disabled',
            'stargazers_count',
            'watchers_count',
            'forks',
            'owner',
        ]


class RepositoryListSerializer(RepositorySerializer):
    class Meta:
        model = core_models.Repository
        fields = [
            'github_id',
            'name',
            'html_url',
            'git_url',
        ]
