from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Importamos models
from catalog.models import Producto
from carreto.models import Carreto
from catalog.serializers import ProductoSerializer


from .serializers import *


@api_view(['GET'])
def lista_carrito(request):
    if request.method == 'GET':
        carrito = Carreto.objects.all()
        serializer = ProductoSerializer(carrito, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def carrito_id(request, ct):
    try:
        carreto = Carreto.objects.get(id=ct)
        serializer = CarretoSerializer(
            carreto, context={'request': request}, many=False)
        return Response(serializer.data)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# add producto al carrito, creamos un array de id, obtemos los productos de la app Catalogo por ids
@api_view(['POST'])
def add_carrito(request, productosB):
    if request.method == 'POST':
        productosB = request.data.get('productosB', '')
        # Crea una lista de IDs de productos
        listProduct = [int(e) for e in productosB.split(",")]
        # Obtiene los productos de la app "Productos" por sus IDs
        myProducts = Producto.objects.filter(idProducte__in=listProduct)
        # Crea un carreto con la propiedad isBuy establecida en False
        carr = Carreto(isBuy=True)
        carr.save()
        # Asigna los productos al carreto
        carr.productes.set(myProducts)
        return Response({'error': 'Carreto creado'}, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# modif product carrito, los datos de cada producto se de modificaran agusto del cliente,
# en el caso que exista el producto, guardaremos los cambios
@api_view(['GET', 'PUT'])
def modif_carrito(request, ct):
    try:
        item = Carreto.objects.get(id=int(ct))
        items = request.data.get('items', [])
        myItems = Producto.objects.filter(id__in=items)
        item.Productos.clear()
        item.Productos.add(*myItems)
        return Response(status=status.HTTP_200_OK, content_type='application/json')
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, content_type='application/json')

# elimina carreto, enviaremos un error en el caso q no exista


@api_view(['GET', 'DELETE'])
def delete_all_carrito(request, ct):
    try:
        carreto = Carreto.objects.get(id=ct)
        carreto.delete()
        return render(status=status.HTTP_204_NO_CONTENT)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
