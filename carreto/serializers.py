from rest_framework import serializers

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Carreto
from .serializers import *
from catalog.serializers import ProductoSerializer

#Los serializadores en Django son una forma de convertir modelos y 
# otros tipos de datos en representaciones legibles y manipulables, ç
# como JSON, XML o incluso una representación en HTML.
class CarretoSerializer(serializers.ModelSerializer):
    productos =  ProductoSerializer(many=True)
    class Meta:
        model = Carreto
        fields = ('idCarreto', 'nombreCarreto', 'productos')