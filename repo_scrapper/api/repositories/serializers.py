from rest_framework import serializers

from repo_scrapper.core import models as core_models


class RepositorySerializer(serializers.ModelSerializer):
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
