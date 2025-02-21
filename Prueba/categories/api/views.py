from rest_framework.viewsets import ModelViewSet
from categories.models import Tours,Activities
from categories.api.serializers import CategoryTourSerializer, CategoryActsSerializer
from categories.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryToursApiView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryTourSerializer
    queryset = Tours.objects.all()
    #Traer solo los disponibles
    #queryset = Tours.objects.filter(disponibilidad=True)
    lookup_field = 'nombre'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['disponibilidad', 'nombre']

class CategoryActsApiView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategoryActsSerializer
    queryset = Activities.objects.all()
    lookup_field = 'nombre'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'precio']