from django.urls import include, path
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

urlpatterns = [
    path('repositories/', include('repo_scrapper.api.repositories.urls')),
]

app_name = "api"
urlpatterns += router.urls
