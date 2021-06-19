
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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


@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(request, pk=None):
    """User detail view."""

    user = User.objects.filter(id=pk).first()

    if request.method == "GET":
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()

            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(
            {"message": "Usuario eliminado correctamente"},
            status=status.HTTP_200_OK
        )
