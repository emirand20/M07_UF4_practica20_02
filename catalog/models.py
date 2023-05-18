import uuid
from django.db import models

class Producto(models.Model):
    codigoDeBarras = models.CharField(max_length=32, default=uuid.uuid4().hex, editable=False, unique=True)
    codigo = models.CharField(max_length=6, unique=True, default=uuid.uuid4().hex[:6])
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    caducidad = models.DateField(default='2023-12-31')
    descripcion = models.TextField()

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre



# from django.db import models

# class Producto(models.Model):
#     nombre = models.CharField(max_length=64)
#     descripcion = models.CharField(max_length=32)
#     precio = models.FloatField()
#     imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(auto_now=True)

# def __str__(self):
#    return self.nombre