from django_filters import rest_framework as filters

from repo_scrapper.core import models as core_models


class RepositoryFilter(filters.FilterSet):
    """
    filters repository API

    """
    name = filters.CharFilter(lookup_expr='icontains')
    language = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = core_models.Repository
        fields = [
            'name',
            'language',
        ]
