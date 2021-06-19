from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import User
from apps.api.serializers import UserSerializer


class UserApiView(APIView):
    """User list view."""

    def get(self, request):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)

        return Response(user_serializer.data)
