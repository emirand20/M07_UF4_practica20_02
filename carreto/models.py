from django.db import models
from catalog.models import Producto
import uuid

class Carreto(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, default=uuid.uuid4().hex)
    nombreCarreto = models.CharField(max_length=50, default=None)
    productos = models.ManyToManyField(Producto)
    isBuy = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCarreto