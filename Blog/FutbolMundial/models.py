from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
    

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
    
class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='avatares', null = True, blank = True)