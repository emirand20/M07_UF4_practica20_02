from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Pago

        
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('id','numero','fecha','cvc')