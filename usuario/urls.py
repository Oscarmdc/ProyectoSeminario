"""
URL configuration for ProyectoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import index, vistas
from producto.views import addProducto
from proveedor.views import provedores
from categoria.views import categorias
from ubicacion.views import ubicacion

urlpatterns = [
    path('', index, name='index'),
    path('productos/', addProducto, name='add-product'),
    path('proveedores/', provedores, name='add-provider'),
    path('categorias/', categorias, name='add-category'),
    path('ubicacion/', ubicacion, name='add-location'),
    path('vistas/', vistas, name='vistas'),
]