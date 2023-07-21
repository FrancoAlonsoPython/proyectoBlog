from django.db import models
# Create your views here.


class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=400)
    imagen = models.URLField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=60)
    comentario = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nombre
    
