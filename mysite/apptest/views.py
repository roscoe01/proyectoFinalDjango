from django.shortcuts import render

from .models import Producto

from django.shortcuts import render

from django.http import HttpResponse


def paginaInicio(request):
    return render (request, "index.html")


def producto_by_id(request, producto_id):
    producto = Producto.objects.get(pk = producto_id)
    return HttpResponse(f"Producto: {producto.nombre} - Precio: {producto.precio} - Stock: {producto.stock}")

def productos(request):
    return render (request, "productos.html")