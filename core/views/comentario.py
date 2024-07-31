from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Comentario
from core.serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all().order_by("id")
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['avaliacao'] 
    search_fields = ['avaliacao']  
    ordering_fields = ['id', 'avaliacao']