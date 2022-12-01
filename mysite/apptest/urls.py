from django.urls import path

from . import views

urlpatterns = [
    path('producto/<int:producto_id', views.producto_by_id, name = 'producto_by_id'),
]