from django.shortcuts import render
from artistas.models import Artista

# Create your views here.

def home(request):

    return render(request, "webzeroapp/home.html")


def artistas(request):
    artistas = Artista.objects.all()

    return render(request, "webzeroapp/artistas.html",{"artistas":artistas}) 

def tienda(request):

    return render(request, "webzeroapp/tienda.html")

def blog(request):

    return render(request, "webzeroapp/blog.html")

def contacto(request):

    return render(request, "webzeroapp/contacto.html")