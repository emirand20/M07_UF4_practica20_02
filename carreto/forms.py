from django.forms import ModelForm
from .models import Carreto

class CarretoForm(ModelForm):
    class Meta:
        model = Carreto
        fields = '__all__'