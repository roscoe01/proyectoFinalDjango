from django.urls import path

from apptest.views import *

urlpatterns = [
    path('', paginaInicio),
    path('producto/<int:producto_id>', producto_by_id),
    path('productos/', productos),
]