from django.db import models

# Model para la tabla de publicaciones.

class Publicacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    categoria = models.CharField(max_length=50)
    creador =  models.CharField(max_length=50)

    def __str__(self):
       return self.titulo

