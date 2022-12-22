from django.shortcuts import render

from django.shortcuts import render

from .models import *

from django.http import HttpResponse


def paginaInicio(request):
    return render (request, "landingpage.html")


def registro(request):

    if request.method == "POST":
        nombreu = request.POST["username"]
        contra = request.POST["password"] 
        correo = request.POST["email"] 
        nacion = request.POST["pais"] 
        nacimiento = request.POST["fechaNac"] 
        
        usuario = Usuario(nombre=nombreu,email=correo,password=contra,nacionalidad=nacion,fechaNacimiento=nacimiento)
        
        usuario.save()
        
        return render (request, "landingpage.html")


    return render (request, "registro.html")


def pilotos(request):

    allPilotos = Piloto.objects.all()

    return render (request, "pilotos.html", {"pilotos":allPilotos})





def piloto_por_id(request,id):
    
    piloto = Piloto.objects.get(pk=id)

    return render(request, "piloto.html", {"piloto": piloto})
