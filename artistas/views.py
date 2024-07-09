from django.shortcuts import render
from artistas.models import Artista

# Create your views here.

def artistas(request):
    artistas = Artista.objects.all()

    return render(request, "artistas/artistas.html",{"artistas":artistas}) 