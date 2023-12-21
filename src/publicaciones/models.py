from django.db import models
from django.urls import reverse
from users.models import User

# Model para la tabla de publicaciones.

class Categoria(models.Model):
   nombre=models.CharField(max_length=50)

   def __str__(self):
      return self.nombre

class Publicacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='publicaciones', null=True)
    creador =  models.ForeignKey(User, related_name='publicaciones', on_delete=models.CASCADE)

    def __str__(self):
       return self.titulo
    
    def get_absolute_url(self):
       return reverse('posts')

