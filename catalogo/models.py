from django.db import models

from artistas.models import Artista

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='catalogo')
    precio = models.IntegerField()
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE,db_column='nombreArtista')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,db_column='nombreCategoria')

    def __str__(self):
        return self.nombre