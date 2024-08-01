from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Projeto
from core.serializers import ProjetoSerializer

class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all().order_by("id")
    serializer_class = ProjetoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['titulo'] 
    search_fields = ['titulo']  
    ordering_fields = ['id', 'titulo']