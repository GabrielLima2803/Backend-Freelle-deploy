from rest_framework.serializers import ModelSerializer

from core.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depth = 1

class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'isPro']