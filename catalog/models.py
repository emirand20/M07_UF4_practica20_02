# Imports
import uuid
from django.db import models

# Creacion de la clase Producto
class Producto(models.Model):

    # Campos para el producto:
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    caducidad = models.DateField(default='2023-12-31')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre