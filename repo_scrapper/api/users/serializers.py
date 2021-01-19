from rest_framework import serializers

from repo_scrapper.core import models as core_models


class GitHubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.User
        fields = [
            'github_id',
            'login',
            'url',
        ]
