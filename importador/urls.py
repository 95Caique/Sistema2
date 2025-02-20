from django.urls import path
from .views import importar_servidor_view

urlpatterns = [
    path('', importar_servidor_view, name='importar-servidor'),
]
