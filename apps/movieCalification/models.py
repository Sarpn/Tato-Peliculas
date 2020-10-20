from django.db import models
from ..login.models import Usuario

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    sinopsis =  models.TextField()
    autor =  models.CharField(max_length=200)
    anio =  models.IntegerField()
    imagen =  models.ImageField(upload_to='imagenes/')
    
    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    valor = models.IntegerField()