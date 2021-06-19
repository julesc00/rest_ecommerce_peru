from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serialize the user object."""

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id",)
