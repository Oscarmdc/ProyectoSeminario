from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Proveedores


# Create your views here.

def provedores(request):

    form_proveedor = modelform_factory(Proveedores, exclude=[])

    if request.method == 'POST':
        proveedor = form_proveedor(request.POST)

        if proveedor.is_valid():
            proveedor.save()
            return redirect('index')
        else:
            return render(request, 'add-provider.html', {'form_proveedor': proveedor})
    else:
        proveedor = form_proveedor()
        return render(request, 'add-provider.html', {'form_proveedor': proveedor})