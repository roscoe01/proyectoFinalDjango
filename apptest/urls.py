from django.urls import path

from apptest.views import *


urlpatterns = [
    path('', paginaInicio, name="inicio"),
    path('pilotos/', pilotos, name="pilotos"),
    path('registro', registro, name="registro"),
    path('piloto/<id>', piloto_por_id, name="piloto")
]