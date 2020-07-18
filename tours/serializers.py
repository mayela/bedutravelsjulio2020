from rest_framework import serializers

from .models import Tour, User, Zona


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('genero', 'tipo')

class TourSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tour
        fields = ('nombre', 'descripcion')
        
class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    tours_salida = TourSerializer(many=True, read_only=True)
    tours_llegada = TourSerializer(many=True, read_only=True)
    class Meta:
        model = Zona
        fields = ('nombre', 'tours_salida', 'tours_llegada')

