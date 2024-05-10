from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from .models import Productos
from .form import FormProductos


# Create your views here.
def addProducto(request):

    form_producto = modelform_factory(Productos, exclude=[])

    if request.method == 'POST':

        producto = form_producto(request.POST)

        if producto.is_valid():
            producto.save()
            return redirect('index')
        else:
            return render(request, 'productos/add-product.html', {'form_producto': producto})
    else:
        producto = form_producto()
        return render(request, 'productos/add-product.html', {'form_producto': producto})


def editProducto(request, id):

    producto = get_object_or_404(Productos, pk=id)

    if request.method == 'POST':
        formProductos = FormProductos(request.POST, instance=producto)
        if formProductos.is_valid():
            formProductos.save()
            return redirect('index')
        else:
            return render(request, 'productos/edit-product.html', {'form_productos': formProductos})
    else:
        producto = get_object_or_404(Productos, pk=id)
        formProducto = FormProductos(instance=producto)
        return render(request, 'productos/edit-product.html', {'form_producto': formProducto})


def getProductos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/list-products.html', {"productos": productos})


def deleteProducto(request, id):
    producto = get_object_or_404(Productos, pk=id)
    if producto:
        producto.delete()
        return redirect('index')
    pass
