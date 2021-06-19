from django.urls import path

from apps.api.api import user_api_view

app_name = "api"

urlpatterns = [
    path("users/", user_api_view, name="users"),
]
