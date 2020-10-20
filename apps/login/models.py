from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    nombreDeUsuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre