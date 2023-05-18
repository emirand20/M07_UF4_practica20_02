from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comandes, Carreto, User
from .serializers import ComandesSerializer

# Ver todas las comandas
@api_view(['GET'])
def lista_comandas(request):
    # Obtenemos los datos de comandes
    data = Comandes.objects.all()
     # Pedimos datos y hacemos filtrado 
    serializer = ComandesSerializer(data, context={'request': request}, many=True)
    # devolvemos el serializer
    return Response({'result': serializer.data})

# Ver comanda
@api_view(['GET'])
def ver_comanda(request, pk):
    try:
        # Obtener datos específicos por id
        data = Comandes.objects.get(idComanda=pk)
        serializer = ComandesSerializer(data, context={'request': request}, many=False)
        # devolvemos la comanda
        return Response({'comanda': serializer.data})
    except Comandes.DoesNotExist:
        return Response({'error': 'La comanda no existe'}, status=status.HTTP_404_NOT_FOUND)

# Añadir una comanda
@api_view(['POST'])
def agregar_comanda(request):
     # Obtenemos los datos de usuario y carretons 
    user_id = request.data.get('user')
    carretons = request.data.get('carretons')

    # Convertimos la cadena de carretons en una lista de enteros
    lista_carrito = [int(e) for e in carretons.split(",")]
    # Obtenemos el usuario por id
    isUser = User.objects.get(idUser=user_id)
    # almacenamos en una variable la comanda con el usuario
    command = Comandes(user=isUser)
    command.save()
    # asignamos la lista de carretons a comandas
    command.carretons.set(lista_carrito)

    return Response({'success': 'Comanda creada con éxito'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def elimina_comanda(request, idC):
    prodct = Comandes.objects.filter(carrito=idC)
    prodct.delete()
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