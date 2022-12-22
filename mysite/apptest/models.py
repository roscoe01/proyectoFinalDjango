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

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    paisOrigen = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    chasis = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    neumaticos = models.CharField(max_length=50)
    debut =  models.IntegerField()
    campeonatos =  models.IntegerField()




class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()



