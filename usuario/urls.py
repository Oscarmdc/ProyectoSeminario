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

import proveedor
from .views import index, vistas
from producto.views import addProducto, editProducto, getProductos, deleteProducto
from proveedor.views import addProvedor, editProveedor, getProveedores, deleteProveedor
from categoria.views import addCategoria, editCategoria, getCategorias, deleteCategoria
from ubicacion.views import addUbicacion, editUbicacion, getUbicaciones, deleteUbicacion

urlpatterns = [
    path('', index, name='index'),

    path('nuevo-producto/', addProducto, name='add-product'),
    path('editar-producto/<int:id>', editProducto, name='edit-product'),
    path('lista-productos/', getProductos, name='list-products'),
    path('eliminar-producto/<int:id>', deleteProducto, name='delete-product'),

    path('nuevo-proveedor/', addProvedor, name='add-provider'),
    path('editar-proveedor/<int:id>', editProveedor, name='edit-provider'),
    path('lista-proveedores/', getProveedores, name='list-provider'),
    path('eliminar-proveedor/<int:id>', deleteProveedor, name='delete-provider'),

    path('nueva-categoria/', addCategoria, name='add-category'),
    path('editar-categoria/<int:id>', editCategoria, name='edit-category'),
    path('lista-categorias/', getCategorias, name='list-category'),
    path('eliminar-categoria/<int:id>', deleteCategoria, name='delete-category'),

    path('nueva-ubicacion/', addUbicacion, name='add-location'),
    path('editar-ubicacion/<int:id>', editUbicacion, name='edit-location'),
    path('lista-ubicaciones/', getUbicaciones, name='list-location'),
    path('editar-ubicacion/<int:id>', deleteUbicacion, name='delete-location'),

    path('vistas/', vistas, name='vistas'),
]