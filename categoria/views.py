from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from .models import Categorias
from .form import FormCategoria


# Create your views here.
def addCategoria(request):

    form_categoria = modelform_factory(Categorias, exclude=[])

    if request.method == 'POST':
        categoria = form_categoria(request.POST)

        if categoria.is_valid():
            categoria.save()
            return redirect('index')
        else:
            return render(request, 'categorias/add-category.html', {'form_categoria': categoria})
    else:
        categoria = form_categoria()
        return render(request, 'categorias/add-category.html', {'form_categoria': categoria})


def editCategoria(request, id):

    categoria = get_object_or_404(Categorias, pk=id)

    if request.method == 'POST':
        form_categoria = FormCategoria(request.POST, instance=categoria)
        if form_categoria.is_valid():
            form_categoria.save()
            return redirect('index')
        else:
            return render(request, 'categorias/edir-category.html', {'form_categoria': form_categoria})
    else:
        categoria = get_object_or_404(Categorias, pk=id)
        form_categoria = FormCategoria(instance=categoria)
        return render(request, 'categorias/edir-category.html', {'form_categoria': form_categoria})


def getCategorias(request):
    categorias = Categorias.objects.all()
    context = {'categorias': categorias}
    return render(request, 'categorias/list-category.html', context)


def deleteCategoria(request, id):
    categoria = get_object_or_404(Categorias, pk=id)
    if categoria:
        categoria.delete()
        return redirect('index')