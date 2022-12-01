"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import *
from apptest.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segundaVista/', segundaVista),
    path('diadehoy/', dia_de_hoy),
    path('saludarconnombre/<nombre>', saludar_con_nombre),
    path('probandohtml/', probando_html),
    path('inicio/', paginaInicio),
    path('producto/', producto),
    path('producto/<int:producto_id>', producto_by_id),


]
