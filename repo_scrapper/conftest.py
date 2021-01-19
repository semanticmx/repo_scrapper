import pytest

from repo_scrapper.core import models as core_models
from repo_scrapper.core.tests.factories import RepositoryFactory, UserFactory


@pytest.fixture
def user() -> core_models.User:
    return UserFactory()


@pytest.fixture
def repo() -> core_models.Repository:
    return RepositoryFactory()
