from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
<<<<<<< Updated upstream
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

#     def __str__(self):
#         return self.nombre
=======
    
def __str__(self):
    return self.nombre

>>>>>>> Stashed changes
