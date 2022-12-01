from django.http import HttpResponse
import datetime

from django.template import Template, Context, loader



def saludo(request):
    return HttpResponse("Hola Mundo")


def segundaVista(request):
    return HttpResponse("Hola soy una segunda vista")


def dia_de_hoy(request):
    dia_de_hoy = datetime.datetime.now()
    cadena=f"Hoy es {dia_de_hoy}"
    return HttpResponse(cadena)


def saludar_con_nombre(request, nombre):
    saludo=f"Hola {nombre}!"
    return HttpResponse(saludo)


def probando_html(request):

    nom = "Cori"

    ape = "Gutman"

    diccionario = {"nombre":nom, "apellido":ape, "notas": [10,2,6,4,7,5,9]}

    plantilla = loader.get_template('template.html')

    documento = plantilla.render(diccionario) #Renderizo el contexto en el template.

    return HttpResponse(documento)


def paginaInicio(request):

    plantilla = loader.get_template('index.html')

    documento = plantilla.render()

    return HttpResponse(documento)