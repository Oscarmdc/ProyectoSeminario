from django.shortcuts import render, redirect
from django.forms import modelform_factory
from .models import Categorias


# Create your views here.
def categorias(request):

    form_categoria = modelform_factory(Categorias, exclude=[])

    if request.method == 'POST':
        categoria = form_categoria(request.POST)

        if categoria.is_valid():
            categoria.save()
            return redirect('index')
        else:
            return render(request, 'add-category.html', {'form_categoria': categoria})
    else:
        categoria = form_categoria()
        return render(request, 'add-category.html', {'form_categoria': categoria})