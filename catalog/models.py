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
    # uuid.uuid4() generara valores aleatorios  + .hex = convierte el UUID en una cadena hexadecimal.
    codigo = models.CharField(max_length=6, unique=True, default=uuid.uuid4().hex[:6])
    codigoDeBarras = models.CharField(max_length=32, default=uuid.uuid4().hex, editable=False, unique=True)

    def __str__(self):

        # Devuelve el nombre del producto como representación en cadena
        return self.nombre