from django.contrib import admin
from django.urls import path, include
from importador.views import importar_servidor_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('importar_servidor/', include('importador.urls')),
    path('', importar_servidor_view, name='importar-servidor'),
]
