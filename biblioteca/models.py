import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='Id de Marca')
    nombreMarca =  models.CharField(max_length=50, verbose_name='Nombre de Marca')

    def __str__(self):
        return self.nombreMarca
    
# AÑADI CATEGORIA CON SU FORANEA DE ARRIBA 
class Galon(models.Model):
    idGalon = models.CharField(primary_key=True, max_length=10, verbose_name='IdGalon')
    kg=models.IntegerField(blank=True, null=True, verbose_name="kg")
    marca = models.ForeignKey ('marca', on_delete=models.CASCADE, verbose_name='marca')
    cantidad=models.IntegerField(blank=True, null=True, verbose_name="Cantidad")
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")


    def __str__(self):
        return self.idGalon

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Galon', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)