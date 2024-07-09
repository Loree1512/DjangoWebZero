from django.shortcuts import render
from .carro import Carro
from catalogo.models import Articulo
from django.shortcuts import redirect

# Create your views here.

def agregar_articulo(request,articulo_id):
    carro=Carro(request)
    articulo=Articulo.objects.get(id=articulo_id)
    carro.agregar(articulo=articulo)
    return redirect ("catalogo")

def eliminar_articulo(request,articulo_id):
    carro=Carro(request)
    articulo=Articulo.objects.get(id=articulo_id)
    carro.eliminar(articulo=articulo)
    return redirect ("catalogo")

def restar_articulo(request,articulo_id):
    carro=Carro(request)
    articulo=Articulo.objects.get(id=articulo_id)
    carro.restar_articulo(articulo=articulo)
    return redirect ("catalogo")

def limpiar_carro(request, articulo_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect ("catalogo")