from django.db import models
from catalog.models import Producto

class Carreto(models.Model):
    productos = models.ManyToManyField(Producto)
    isBuy = models.BooleanField(default=False)
    #suario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"Carreto {self.id}"