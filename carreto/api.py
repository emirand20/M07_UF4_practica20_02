from .models import Carreto
from rest_framework import viewsets, permissions
from .serializers import CarretoSerializer

class CarretoViewSet(viewsets.ModelViewSet):
    queryset = Carreto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarretoSerializer
    