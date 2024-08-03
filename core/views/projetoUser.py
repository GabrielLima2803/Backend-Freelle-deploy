from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from core.models import UserProjeto
from core.serializers import UserProjetoSerializer

class UserProjetoViewSet(ModelViewSet):
    queryset = UserProjeto.objects.all().order_by("id")
    serializer_class = UserProjetoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['projeto'] 
    search_fields = ['projeto']  
    ordering_fields = ['id', 'projeto']