from factory import Faker
from factory.django import DjangoModelFactory

from repo_scrapper.core import models as core_models


class UserFactory(DjangoModelFactory):
    github_id = Faker("pyint")
    login = Faker("name")

    class Meta:
        model = core_models.User
        django_get_or_create = ["login"]


class RepositoryFactory(DjangoModelFactory):
    github_id = Faker("pyint")
    full_name = Faker("name")
    stargazers_count = Faker("pyint")
    watchers_count = Faker("pyint")
    forks = Faker("pyint")

    class Meta:
        model = core_models.Repository
        django_get_or_create = ["full_name"]
