from django.forms import ModelForm
from catalog.models import Producto

class CarretoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'