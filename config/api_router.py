from django.urls import include, path


app_name = "api"

urlpatterns = [
    path('repositories/', include('repo_scrapper.api.repositories.urls')),
    path('users/', include('repo_scrapper.api.users.urls')),
]
