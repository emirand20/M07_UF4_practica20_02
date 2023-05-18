from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comandes, Carreto, User
from .serializers import ComandesSerializer

#Ver todas las comandas
@api_view(['GET', 'POST'])
def lista_comandas(request):
    if request.method == 'GET':
        # obtenemos los datos del modelo Comandes
        data = Comandes.objects.all()
        # adaptamos los datos obtenido y le damos un contexto
        serializer = ComandesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # adaptamos las request
        serializer = ComandesSerializer(data=request.data)
        # validamos y guardamos
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Ver comanda
@api_view(['GET'])
def ver_comanda(request, pk):
    try:
        # obtenemos datos especificos por id
        data = Comandes.objects.get(idComanda = pk)
        serializer = ComandesSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    except Comandes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

#Añadir una comanda
@api_view(['GET', 'POST'])
def agregar_comanda(request, user, carretons):
    # convertimos la cadena en en enteros
    lista_carrito = [int(e) for e in carretons.split(",")]
    # guardamos los datos del modelo user en uno especifico
    isUser = User.objects.get(idUser = user)
    # lo mismo pero ahora con el modelo comandes
    command = Comandes(user=isUser)
    command.save()
    command.carretons.set(lista_carrito)
    return Response({'success': 'Comanda creada con exito'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def elimina_comanda(request, idC):
    product = Comandes.objects.filter(carrito=idC)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Crea una comanda, de manera que verificamos si la comanda existe, primeramente hacemos un listado,
#la filtramos y creamos la nueva comanda.

@api_view(['PUT'])
def comanda_modif(request, comId):
    try:
        comanda = Comandes.objects.get(idComanda=int(comId))
        carritos = request.data.get('carritos', [])
        myCarritos = Carreto.objects.filter(idCarreto__in=carritos)
        comanda.carretons.set(myCarritos)
        comanda.save()
        serializer = ComandesSerializer(comanda, context={'request': request})
        return Response(serializer.data)
    except Comandes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

#Muesta el historial de la compra del usuario, primeramente buscamos el usuario por su idm filtra
#la comanda para el usuario y si no existe error.
@api_view(['GET'])
def historialComanda_user(request, idC):
    myUser = User(User, idUser=int(idC))
    myComanda = Comandes.objects.filter(user=myUser).first()
    
    if myComanda:
        serializer = ComandesSerializer(myComanda, context={'request': request})
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)