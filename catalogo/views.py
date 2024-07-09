from django.shortcuts import render
from catalogo.models import Articulo
# Create your views here.

def catalogo(request):
    articulos = Articulo.objects.all()
    return render(request, "catalogo/catalogo.html", {"articulos":articulos})