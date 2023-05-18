# Imports
from rest_framework import serializers
from .models import Producto

# Creacion de la clase ProductoSerializer
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        # Se define el modelo asociado al serializador
        model = Producto
        # Se incluyen todos los campos del modelo en el serializador
        fields = '__all__'


