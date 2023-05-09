from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'



# from rest_framework import serializers
# from .models import Producto

# class ProductoSerializer(serializers.ModelSerializer):
#     imagen = serializers.ImageField(max_length=None, use_url=True)

#     class Meta:
#         model = Producto
#         fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'fecha_creacion', 'fecha_actualizacion']
#         read_only_fields = ['fecha_creacion', 'fecha_actualizacion']
