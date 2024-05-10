from django.shortcuts import render, redirect


# Create your views here.

# vista principal de la pagina web
def index(request):
    return render(request, 'menu.html')


def login(request):
    context = {}
    return render(request, 'registration/login.html', context)


def vistas(request):
    context = {}
    return render(request, 'vista.html', context)
