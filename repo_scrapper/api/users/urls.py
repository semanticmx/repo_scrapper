from django.urls import path

from . import views as user_views


app_name = "users"

urlpatterns = [
    path('', user_views.GitHubUserList.as_view(), name='all'),
    path('<int:github_id>/', user_views.GitHubUserDetails.as_view(), name='detail'),
]
