import logging

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView

from repo_scrapper.core import models as core_models
from repo_scrapper.api.filters import RepositoryFilter
from.serializers import RepositorySerializer, RepositoryListSerializer

logger = logging.getLogger(__name__)


class RepositoryList(ListAPIView):
    """
    List all repositories

    """
    serializer_class = RepositoryListSerializer
    queryset = core_models.Repository.objects.all()
    filterset_class = RepositoryFilter


class RepositoryDetails(GenericAPIView):
    """
    Returns repository info by github id

    """
    queryset = core_models.Repository.objects.all()
    lookup_field = 'github_id'

    def get(self, request, github_id):
        serializer = RepositorySerializer(self.get_object())
        return Response(serializer.data)
