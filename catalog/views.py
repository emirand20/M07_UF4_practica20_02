import statistics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Producto
from .serializers import ProductoSerializer
from django.views.decorators.csrf import csrf_exempt    

@api_view(['GET'])
def lista_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
def agregar_producto(request):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)  

@api_view(['GET', 'PUT', 'PATCH'])
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=statistics.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return Response(status=204)
