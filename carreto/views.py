from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Importamos models
from catalog.models import Producto
from carreto.models import Carreto
from catalog.serializers import ProductoSerializer


from .serializers import *
from django.http import JsonResponse




@api_view(['GET', 'POST'])
def lista_carrito(request):
    if request.method == 'GET':
        data = Producto.objects.all()
        serializer = ProductoSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def carrito_id(request, ct):
    try:
        data = Producto.objects.get(id=ct)
        serializer = ProductoSerializer(
            data, context={'request': request}, many=False)
        return Response(serializer.data)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# add producto al carrito, si el es valido con el post, enviara el formulario, reenviara al template
@api_view(['GET', 'POST'])
def add_carrito(request, items):
    listaProductos = [int(e) for e in items.split(",")]
    myItems = Producto.objects.filter(id=listaProductos)

    cart = Carreto(isBuy=False)
    cart.save()
    cart.productes.set(myItems)
    return Response({'success': 'Carrito añadido'}, status=status.HTTP_201_CREATED)

# modif product carrito, los datos de cada producto se de modificaran agusto del cliente, 
# en el caso que exista el producto, guardaremos los cambios
@api_view(['GET', 'PUT', 'POST'])
def modif_carrito(request, ct, items):
    try:
        item = Carreto.objects.get(id=int(ct))
        listaProductos = [int(e) for e in items.split(",")]
        myItems = Producto.objects.filter(id=listaProductos)
        item.save()
        item.productos.set(myItems)
        serializer = CarretoSerializer(item, context={'request': request})
        return Response(serializer.data)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#elimina carreto, enviaremos un error en el caso q no exista
@api_view(['GET','DELETE'])
def delete_all_carrito(request,ct):
    try:
        carreto = Carreto.objects.get(id = ct)
        carreto.delete()
        return render(status=status.HTTP_204_NO_CONTENT)   
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)