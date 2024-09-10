from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Projeto

class ProjetoSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = "__all__"

class ProjetoDetailSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = "__all__"
        depth = 1

class ProjetoListSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'status', 'categoria']