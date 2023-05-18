from django.db import models

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField('Tarjeta', max_length = 100)
    fecha = models.DateField('Fecha')
    cvc = models.CharField('CVC', max_length = 3)

    def __str__(self):
        return  '{0},{1},{2}'.format(self.numero, self.fecha, self.cvc)
