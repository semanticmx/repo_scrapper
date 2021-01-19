import pytest

from django.test import RequestFactory

from repo_scrapper.core import models as core_models
from repo_scrapper.api.repositories import views as repo_views


pytestmark = pytest.mark.django_db


class TestUserList:
    def test_get_all(self, rf: RequestFactory):
        request = rf.get("/fake-url/")

        response = repo_views.RepositoryList.as_view()(request)

        assert response.status_code == 200

    def test_get_details(self, repo: core_models.Repository, rf: RequestFactory):
        request = rf.get("/fake-url/")

        response = repo_views.RepositoryDetails.as_view()(request, github_id=repo.github_id)

        assert response.status_code == 200

    def test_invalid_repo_id(self, rf: RequestFactory):
        request = rf.get("/fake-url/")

        response = repo_views.RepositoryDetails.as_view()(request, github_id=1)

        assert response.status_code == 404
