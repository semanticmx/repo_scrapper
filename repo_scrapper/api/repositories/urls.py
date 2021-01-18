from django.urls import path

from .views import RepositoryList, RepositoryDetails

urlpatterns = [
    path('', RepositoryList.as_view(), name='all'),
    path('<int:github_id>/', RepositoryDetails.as_view(), name='detail'),
]
