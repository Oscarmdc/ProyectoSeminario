from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Productos


# Create your views here.



def addProducto(request):
    form_producto = modelform_factory(Productos, exclude=[])

    if request.method == 'POST':

        producto = form_producto(request.POST)

        if producto.is_valid():
            producto.save()
            return redirect('index')
        else:
            return render(request, 'add-product.html', {'form_producto': producto})
    else:
        producto = form_producto()
        return render(request, 'add-product.html', {'form_producto': producto})