from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.api.serializers import UserSerializer


@api_view(["GET"])
def user_api_view(request):
    """User list view."""

    if request.method == "GET":
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)

        return Response(user_serializer.data)
