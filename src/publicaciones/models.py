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
    imagen = models.ImageField(upload_to='imagen-post', blank=True)
    link_compra = models.TextField(null=True, blank=True)
    me_gusta = models.ManyToManyField(User,related_name='posts', blank=True)

    def __str__(self):
       return self.titulo
    
    def get_absolute_url(self):
       return reverse('posts')



class Comentario(models.Model):
   fecha = models.DateField(auto_now_add=True)
   texto = models.TextField()
   publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
   creador =  models.ForeignKey(User, related_name='comentarios', on_delete=models.CASCADE)

   def __str__(self):
      return self.publicacion.titulo + "-"+ self.creador.username
   