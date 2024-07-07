from django.db import models

# Create your models here.

class Artista (models.Model):
    rut=models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    aPaterno = models.CharField(max_length=20)
    aMaterno = models.CharField(max_length=20)
    fechaNacimiento = models.DateField(blank=False, null=False)
    email= models.EmailField(unique=True, max_length=100, blank=True, null=True) 
    telefono = models.CharField(max_length=45)
    foto = models.ImageField(upload_to='artistas')

def __str__(self):
    return self.nombre