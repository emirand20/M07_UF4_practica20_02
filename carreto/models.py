from django.db import models
from catalog.models import Producto

# Create your models here.
class Carreto(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nombreCarreto =  models.CharField(max_length=50,default=None)
    productos = models.ManyToManyField(Producto)
    isBuy = models.BooleanField(default=False)
