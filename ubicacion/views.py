from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Ubicaciones

# Create your views here.
def ubicacion(request):
    form_ubicacion = modelform_factory(Ubicaciones, exclude=[])
    if request.method == 'POST':
        ubicacion = form_ubicacion(request.POST)

        if ubicacion.is_valid():
            ubicacion.save()
            return redirect('index')
        else:
            return render(request, 'add-location.html', {'form_ubicacion': ubicacion})
    else:
        ubicacion = form_ubicacion()
        return render(request, 'add-location.html', {'form_ubicacion': ubicacion})