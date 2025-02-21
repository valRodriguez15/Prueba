from rest_framework import serializers
from categories.models import Tours, Activities
from users.api.serializers import UserSerializer

class CategoryTourSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Tours
        fields = ['id', 'nombre', 'descripcion', 'precio', 'disponibilidad', 'ubicacion', 'user']

class CategoryActsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ['id','nombre','detalle','precio','horario','edadMin', 'tour']

        def validate_tour(self, value):
            if not value.disponibilidad:
                raise serializers.ValidationError('La actividad solo puede ser agregada a tours disponibles.')
            return value
