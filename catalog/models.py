# Imports
from django.db import models

# Creacion de la clase Producto
class Producto(models.Model):

    # Campos para el producto:
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()

    categoria = models.CharField(max_length=50, default='Otros')
    marca = models.CharField(max_length=50, default='Otros')
    garantia = models.TextField(max_length=2, default='No')

    def __str__(self):
        return self.nombre