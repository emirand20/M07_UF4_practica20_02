from rest_framework import serializers
from .models import Comandes
from carreto.serializers import CarretoSerializer

class ComandesSerializer(serializers.ModelSerializer):

    carretons =  CarretoSerializer(many=True)
    class Meta:
        model = Comandes
        fields = ('idComanda', 'user','carretons')