import uuid
from django.db import models

class Producto(models.Model):
    codigoDeBarras = models.CharField(max_length=32, default=uuid.uuid4().hex, editable=False, unique=True)
    codigo = models.CharField(max_length=6, unique=True, default=uuid.uuid4().hex[:6])
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    caducidad = models.DateField(default='2023-12-31')
    descripcion = models.TextField()
    def __str__(self):
    return self.nombre