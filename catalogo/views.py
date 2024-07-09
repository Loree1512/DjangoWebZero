from django.shortcuts import render
from .models import Articulo
# Create your views here.

def catalogo(request):
    articulos = Articulo.objects.all()
    return render(request, "catalogo/catalogo.html", {"articulos":articulos})