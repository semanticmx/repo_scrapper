import pytest

from django.test import RequestFactory

from repo_scrapper.core import models as core_models
from repo_scrapper.api.users import views as users_views
from repo_scrapper.core.tests.factories import UserFactory


pytestmark = pytest.mark.django_db


class TestUserList:
    def test_get_success_url(self, user: core_models.User, rf: RequestFactory):
        request = rf.get("/fake-url/")

        response = users_views.GitHubUserList.as_view()(request)

        assert response.status_code == 200

    def test_get_details(self, user: core_models.User, rf: RequestFactory):
        request = rf.get("/fake-url/")

        response = users_views.GitHubUserDetails.as_view()(request, github_id=user.github_id)

        assert response.status_code == 200

    def test_user_not_found(self, user: core_models.User, rf: RequestFactory):
        request = rf.get("/fake-url/")

        response = users_views.GitHubUserDetails.as_view()(request, github_id=1)

        assert response.status_code == 404
