from django.shortcuts import render
from .models import Producto
from django.http import HttpResponse
# Create your views here.

def producto(request):
    producto = Producto(nombre="Camiseta Scuderia Ferrari 2022 Team Charles Leclerc", precio = 50, stock = 9 )
    producto.save()
    cadena = "Producto guardado: " + producto.nombre
    return HttpResponse(cadena)


def producto_by_id(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    return HttpResponse(f"Producto: {producto.nombre}, - Precio: {producto.precio}, - Stock: {producto.stock}")