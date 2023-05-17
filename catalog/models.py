# Imports
from django.db import models

# Creacion de la clase Producto
class Producto(models.Model):

    # Campos para el producto:
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    garantia = models.TextField(max_length=2)


    def __str__(self):

        # Devuelve el nombre del producto como representación en cadena
        return self.nombre