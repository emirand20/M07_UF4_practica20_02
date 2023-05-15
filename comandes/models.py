from django.db import models
from carreto.models import Carreto
# from login.models import User


class Comandes(models.Model):
    # #Creamos un id para las diferentes comandas por ahora estara comentada esperando el login
    # idComandes = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    #Cada comanda te diferent carretons
    carretons = models.ManyToManyField(Carreto)
    # #Esta sera la comanda del usuario tambien esperando el login
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return "{} - {}".format(self.idComanda, self.carretons, self.user)