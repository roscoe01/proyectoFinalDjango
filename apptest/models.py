from django.db import models
from django.conf import settings
from datetime import datetime



user = settings.AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models


class Piloto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero = models.IntegerField()
    nacionalidad = models.CharField(max_length=50)
    nacimiento = models.DateField()
    campeonatos = models.IntegerField()
    equipo = models.CharField(max_length=50)
    imagen = models.ImageField(null = True, blank= True, upload_to='img')

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    paisOrigen = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    chasis = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    neumaticos = models.CharField(max_length=50)
    debut =  models.IntegerField()
    campeonatos =  models.IntegerField()

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    contenido = models.TextField(max_length=5000)
    horario = models.DateTimeField(auto_now_add=True)