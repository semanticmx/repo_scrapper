import logging

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from repo_scrapper.core import models as core_models
from.serializers import GitHubUserSerializer

logger = logging.getLogger(__name__)


class GitHubUserList(GenericAPIView):
    """
    List all github users

    """
    queryset = core_models.User.objects.all()

    def get(self, request):
        serializer = GitHubUserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class GitHubUserDetails(GenericAPIView):
    """
    Returns github user info by github id

    """
    queryset = core_models.User.objects.all()
    lookup_field = 'github_id'

    def get(self, request, github_id):
        serializer = GitHubUserSerializer(self.get_object())
        return Response(serializer.data)
