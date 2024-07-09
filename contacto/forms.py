from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label= "Nombre", max_length=50)
    email = forms.CharField(label= "Mail" , max_length=50)
    contenido = forms.CharField(label= "Contenido")