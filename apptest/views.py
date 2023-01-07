from django.shortcuts import render

from .models import *

from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from apptest.forms import UsuarioForm, MensajeForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def paginaInicio(request):
    return render (request, "landingpage.html")



@login_required
def pilotos(request):

    allPilotos = Piloto.objects.all()

    return render (request, "pilotos.html", {"pilotos":allPilotos})




@login_required
def piloto_por_id(request,id):
    
    piloto = Piloto.objects.get(pk=id)

    return render(request, "piloto.html", {"piloto": piloto})



def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST) ## Traigo el formulario lleno.

        if form.is_valid():
            user = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            usuario = authenticate(username=user,password=contra) #Busca un usuario con esas credenciales, si no lo existe trae none.

            if usuario is not None:
                login(request,usuario)
                return render(request, 'landingpage.html', {'mensaje':f"{usuario}"})
            else:
                return render(request, 'login.html', {'mensaje':f"Usuario o contraseña incorrectos","form":form})

        else:
            return render(request, 'login.html', {'mensaje':f"Usuario o contraseña incorrectos","form":form})

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form":form})




def registro(request):
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data.get("username")
            form.save()
            return render(request, 'login.html' , {"exito": f"Usuario {username} creado correctamente, porfavor inicia sesión"})
        else:
            print(form.errors)
            print(form.cleaned_data)
            return render(request, 'registro.html' , {"form":form, "mensaje": "Error al crear el usuario, intentalo nuevamente"})


    else:
        form=UsuarioForm()
    
    return render(request, "registro.html", {"form":form})


def terminosycondiciones(request):
    return render(request, "terminosycondiciones.html")


@login_required
def mensajes(request):
    return render(request, 'mensajes.html')


@login_required
def enviarMensaje(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        formulario = MensajeForm()
        
        if form.is_valid():
            info = form.cleaned_data
            print(info)

            
            destinatario = info['receptor']
            contenido = info['mensaje']
            

            mensaje = Mensaje(emisor=(usuario), receptor= (destinatario), contenido=contenido)
            mensaje.save()

            return render(request, 'enviarMensaje.html', {"form": formulario, "mensaje": "Mensaje enviado exitosamente!"} )
        else:
            return render(request, 'landingPage.html', {"mensaje": "Hubo un error en el formulario, vuelve a intentarlo y no olvides rellenar todos los campos!"} )

    else:
        formulario = MensajeForm()
       
    return render(request, 'enviarMensaje.html', {"form": formulario} )

    
@login_required
def mensajesRecibidos(request):
    usuario = request.user
    mensajes = Mensaje.objects.filter(receptor = usuario)
    
    return render(request, "mensajesRecibidos.html", {"mensajes": mensajes})
    
@login_required
def mensajesEnviados(request):
    usuario = request.user
    mensajes = Mensaje.objects.filter(emisor = usuario)
    
    return render(request, "mensajesEnviados.html", {"mensajes": mensajes})