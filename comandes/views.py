from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Comandes, Carreto, User
from .serializers import ComandesSerializer
# Create your views here.

@api_view(['GET', 'DELETE'])
def comanda_borrar(request, idC):
    prod = Comandes.objects.filter(carrito=idC)
    prod.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Crea una comanda, de manera que verificamos si la comanda existe, primeramente hacemos un listado,
#la filtramos y creamos la nueva comanda.
@api_view(['GET', 'PUT'])
def comanda_modif(request, comId, carritos):
    try:
        comanda = Comandes.objects.get(idComanda=int(comId))
        comandesList = [int(e) for e in carritos.split(",")]
        myComandes = Carreto.objects.filter(idCarreto__in=comandesList)
        comanda.save()
        comanda.carretons.set(myComandes)
        context = {'request': request}
        serializer = ComandesSerializer(comanda, context)
        return Response(serializer.data)
    except Comandes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

#Muesta el historial de la compra del usuario, primeramente buscamos el usuario por su idm filtra
#la comanda para el usuario y si no existe error.
@api_view(['GET'])
def historialComanda_user(request, idC):
    try:
        myUser = User.objects.get(idUser = int(idC))
        myComanda = Comandes.objects.filter(user=myUser).first()
        context = {'request': request}
        serializer = ComandesSerializer(myComanda, context, many=False)
        return Response(serializer.data)

    except User.DoesNotExist:
        #Si la comando no existeix
        return Response(status=status.HTTP_404_NOT_FOUND)