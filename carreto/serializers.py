from rest_framework import serializers

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Carreto
from .serializers import *
from catalog.serializers import ProductoSerializer

#Sirven para traducir los modelos a otros formatos
class CarretoSerializer(serializers.ModelSerializer):
    productos =  ProductoSerializer(many=True)
    class Meta:
        model = Carreto
        fields = ('id','producto', 'isBuy', 'total')