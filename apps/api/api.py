
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.api.serializers import UserSerializer


@api_view(["GET", "POST"])
def user_api_view(request):
    """User list view."""

    if request.method == "GET":
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)

        return Response(user_serializer.data)
    elif request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()

            return Response(user_serializer.data)
        return Response(user_serializer.errors)
