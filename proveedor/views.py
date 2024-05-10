from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from .models import Proveedores
from .form import FormProveedor



# Create your views here.

def addProvedor(request):

    form_proveedor = modelform_factory(Proveedores, exclude=[])

    if request.method == 'POST':
        proveedor = form_proveedor(request.POST)

        if proveedor.is_valid():
            proveedor.save()
            return redirect('index')
        else:
            return render(request, 'proveedores/add-provider.html', {'form_proveedor': proveedor})
    else:
        proveedor = form_proveedor()
        return render(request, 'proveedores/add-provider.html', {'form_proveedor': proveedor})

def editProveedor(request, id):
    proveedor = get_object_or_404(Proveedores, pk=id)

    if request.method == 'POST':
        form_proveedor = FormProveedor(request.POST, instance=proveedor)
        if form_proveedor.is_valid():
            form_proveedor.save()
            return redirect('index')
        else:
            return render(request, 'proveedores/edit-provider.html', {'form_proveedor': form_proveedor})
    else:
        proveedor = get_object_or_404(Proveedores, pk=id)
        form_proveedor = FormProveedor(instance=proveedor)
        return render(request, 'proveedores/edit-provider.html', {'form_proveedor': form_proveedor})


def getProveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'proveedores/list-providers.html', {'proveedores': proveedores})


def deleteProveedor(request, id):
    proveedor = get_object_or_404(Proveedores, pk=id)
    if proveedor:
        proveedor.delete()
        return redirect('index')