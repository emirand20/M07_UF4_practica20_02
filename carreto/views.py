from django.shortcuts import render,redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Importamos models
from .models import Producto, Carreto
from .serializers import CarretoSerializer

from .forms import CarretoForm


@api_view(['GET', 'POST'])
def carreto_list(request):
    if request.method == 'GET':
        data = Carreto.objects.all()
        serializer = CarretoSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarretoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''@api_view(['GET', 'POST'])
def carreto_id(request, ct):
    try:  
        data = Carreto.objects.get(idCarreto=ct)
        serializer = CarretoSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#add producto al carrito, si el es valido con el post, enviara el formulario, reenviara al template
@api_view(['GET', 'POST'])
def carreto_add_form(request):
    form = CarretoForm(request.POST)
    context = {'forms':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'carrito.html',context)
    return render(request,'form.html',context)

#modif product carrito, los datos de cada producto se de modificaran agusto del cliente, guardaremos los cambios y reenviara al template
@api_view(['GET', 'PUT','POST'])
def carreto_modify_form(request,ct):
    carreto = Carreto.objects.get(idCarreto = ct)
    form = CarretoForm(instance=carreto)
    context = {'forms':form}
    if request.method == 'POST':
        form = CarretoForm(request.POST, instance=carreto)
    if form.is_valid():
        form.save()
        return render(request,'carrito.html',context)
    return render(request,'form.html',context)

#elimina carreto, enviaremos un error en el caso q no exista
@api_view(['GET','DELETE'])
def carreto_delete(request,ct):
    try:
        carreto = Carreto.objects.get(idCarreto = ct)
        carreto.delete()
        return render(request,'carrito.html')   
    except Carreto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)'''