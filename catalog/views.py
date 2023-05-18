import statistics
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from .models import Producto

@api_view(['GET'])
def lista_productos(request):
    # almacenamos los datos del modelo producto
    productos = Producto.objects.all()
    # adaptacion con serializers 
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_producto(request, pk):
    # obtenemos los datos pero por id
    producto = get_object_or_404(Producto, pk=pk)
    # adaptacion
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)

@api_view(['POST'])
def agregar_producto(request):
    # pedimos los datos especificos de Productos
    serializer = ProductoSerializer(data=request.data)
    # si son aceptados lo guardaremos
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)  

@api_view(['GET', 'PUT', 'PATCH'])
def actualizar_producto(request, pk):
    # obtenemos datos especificos de producto y devuelve error 404 en caso de error
    producto = get_object_or_404(Producto, pk=pk)

    # mirar los datos del producto con get
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    # actualizarlos con put/patch
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=statistics.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminar_producto(request, pk):
    # obtenemos los datos del producto por id
    producto = get_object_or_404(Producto, pk=pk)
    # eliminacion del producto
    producto.delete()
    return Response(status=204)
