import logging

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from repo_scrapper.core import models as core_models
from.serializers import RepositorySerializer, RepositoryListSerializer

logger = logging.getLogger(__name__)


class RepositoryList(GenericAPIView):
    """
    List all repositories

    """
    queryset = core_models.Repository.objects.all()

    def get(self, request):
        serializer = RepositoryListSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class RepositoryDetails(GenericAPIView):
    """
    Returns repository info by github id

    """
    queryset = core_models.Repository.objects.all()
    lookup_field = 'github_id'

    def get(self, request, github_id):
        serializer = RepositorySerializer(self.get_object())
        return Response(serializer.data)
