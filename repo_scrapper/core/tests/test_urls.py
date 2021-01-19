import pytest
from django.urls import resolve, reverse

from repo_scrapper.core import models as core_models

pytestmark = pytest.mark.django_db


def test_all_repos():
    assert (reverse("api:repositories:all") == "/api/repositories/")
    assert resolve("/api/repositories/").view_name == "api:repositories:all"


def test_repo_detail(repo: core_models.Repository):
    assert (reverse("api:repositories:detail", kwargs={"github_id": repo.github_id}))
    assert resolve(f"/api/repositories/{repo.github_id}/").view_name == "api:repositories:detail"


def test_all_users():
    assert (reverse("api:users:all") == "/api/users/")
    assert resolve("/api/users/").view_name == "api:users:all"


def test_user_detail(user: core_models.User):
    assert (reverse("api:users:detail", kwargs={"github_id": user.github_id}))
    assert resolve(f"/api/users/{user.github_id}/").view_name == "api:users:detail"
