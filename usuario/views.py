from django.shortcuts import render


# Create your views here.

# vista principal de la pagina web
def principal(request):
    return render(request, 'menu.html')


def login(request):
    context = {}
    return render(request, 'login.html', context)


def vistas(request):
    context = {}
    return render(request, 'vista.html', context)
