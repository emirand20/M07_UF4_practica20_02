from .models import Carreto
from rest_framework import viewsets, permissions
from .serializers import CarretoSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CarretoViewSet(viewsets.ModelViewSet):
    queryset = Carreto.objects.all()
    serializer_class = CarretoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)



    
    