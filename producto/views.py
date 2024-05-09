from django.shortcuts import render

# Create your views here.

def addProducto(request):
    context = {}
    return render(request, 'add-product.html', context)