from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Favorito
from core.serializers import FavoritoSerializer

class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all().order_by("id")
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['created_at'] 
    search_fields = ['created_at']  
    ordering_fields = ['id', 'created_at']