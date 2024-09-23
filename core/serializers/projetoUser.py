from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .projeto import ProjetoSerializer
from .user import UserSerializer

from core.models import UserProjeto

class UserProjetoSerializer(ModelSerializer):
    fk_client_user = UserSerializer()
    fk_freelancer_user = UserSerializer()
    projeto = ProjetoSerializer()
    class Meta:
        model = UserProjeto
        fields = "__all__"


