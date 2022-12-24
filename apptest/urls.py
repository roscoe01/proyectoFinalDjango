from django.urls import path

from apptest.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', paginaInicio, name="inicio"),
    path('pilotos/', pilotos, name="pilotos"),
    path('registro', registro, name="registro"),
    path('piloto/<id>', piloto_por_id, name="piloto"),
    path('login', login_request , name="login"),
    path('logout', LogoutView.as_view(), name='logout'),
    path('terminosycondiciones', terminosycondiciones, name='terminosycondiciones')
]