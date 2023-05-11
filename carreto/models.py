from django.db import models
from catalog.models import Producto

# Create your models here.
class Carreto(models.Model):
    idCarreto = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nombreCarreto =  models.CharField("nombreCarreto", max_length=50,default=None)
    productos = models.ManyToManyField(Producto)