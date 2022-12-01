from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    ## imagen = models.ImageField() ## Preguntar a tutor como se puede usar esto
    stock = models.IntegerField()


