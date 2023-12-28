from django import forms
from .models import Publicacion,Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo','texto','categoria','imagen']

        labels={
            'texto':'Contale algo a tus seguidores'
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['texto']
        labels={'texto':'Hacé tu comentario acá'}