from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from .models import Ubicaciones
from .form import FormUbicacion

# Create your views here.
def addUbicacion(request):
    form_ubicacion = modelform_factory(Ubicaciones, exclude=[])
    if request.method == 'POST':
        ubicacion = form_ubicacion(request.POST)

        if ubicacion.is_valid():
            ubicacion.save()
            return redirect('index')
        else:
            return render(request, 'ubicaciones/add-location.html', {'form_ubicacion': ubicacion})
    else:
        ubicacion = form_ubicacion()
        return render(request, 'ubicaciones/add-location.html', {'form_ubicacion': ubicacion})

def editUbicacion(request, id):

    ubicacion = get_object_or_404(Ubicaciones, pk=id)

    if request.method == 'POST':
        form_ubicacion = FormUbicacion(request.POST, instance=ubicacion)
        if form_ubicacion.is_valid():
            form_ubicacion.save()
            return redirect('index')
        else:
            return render(request, 'ubicaciones/edit-location.html', {'form_ubicacion': form_ubicacion})
    else:
        ubicacion = get_object_or_404(Ubicaciones, pk=id)
        form_ubicacion = FormUbicacion(instance=ubicacion)
        return render(request, 'ubicaciones/edit-location.html', {'form_ubicacion': form_ubicacion})

def getUbicaciones(request):
    ubicaciones = Ubicaciones.objects.all()
    return render(request, 'ubicaciones/list-locations.html', {"ubicaciones": ubicaciones})

def deleteUbicacion(request, id):
    ubicacion = get_object_or_404(Ubicaciones, pk=id)
    if ubicacion:
        ubicacion.delete()
        return redirect('index')