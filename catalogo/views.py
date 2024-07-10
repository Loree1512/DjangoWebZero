from django.shortcuts import render
from .models import Articulo
# Create your views here.

def catalogo(request):
    articulos = Articulo.objects.all()
    return render(request, "catalogo/catalogo.html", {"articulos":articulos})

def catalogo(request):
    if 'carro' not in request.session:
        request.session['carro'] = {}

    articulos = Articulo.objects.all()  # Asumiendo que tienes un modelo llamado Articulo
    return render(request, "catalogo/catalogo.html", {"articulos": articulos})