from django.shortcuts import render


# Create your views here.

def home(request):

    return render(request, "webzeroapp/home.html")


def tienda(request):

    return render(request, "webzeroapp/tienda.html")



def contacto(request):

    return render(request, "webzeroapp/contacto.html")