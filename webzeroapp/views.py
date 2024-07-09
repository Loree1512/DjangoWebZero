from django.shortcuts import render


# Create your views here.

def home(request):

    return render(request, "webzeroapp/home.html")


def tienda(request):

    return render(request, "webzeroapp/tienda.html")

def blog(request):

    return render(request, "webzeroapp/blog.html")

def contacto(request):

    return render(request, "webzeroapp/contacto.html")