from django.urls import path

from apps.api.api import UserApiView

app_name = "api"

urlpatterns = [
    path("users/", UserApiView.as_view(), name="users"),
]