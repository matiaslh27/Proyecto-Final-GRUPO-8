from typing import Any
from django.shortcuts import render
from .models import Publicacion
from .forms import PostForm,ComentarioForm
from django.views.generic import ListView , CreateView , UpdateView , DeleteView, DetailView
from django.urls import reverse
# Create your views here.
"""def publicaciones_view(request):


    return render(request, 'publicaciones/publicaciones.html', {'publicaciones': Publicacion.objects.all(),})

"""
#View hecha en clase para renderizar las publicaciones desde base de datos
class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'

#View para publicar
class PostView(CreateView):
    template_name='publicaciones/publicar.html'
    model = Publicacion
    form_class = PostForm

    def form_valid(self,form):
        new_form= form.save(commit=False)
        new_form.creador_id=self.request.user.id
        return super().form_valid(new_form)
    
    def get_success_url(self):
        return reverse('posts')

#view para editar una post
class PostEditView(UpdateView):
    template_name='publicaciones/modificar-publicacion.html'
    model = Publicacion
    form_class = PostForm
    success_url = '../ver-publicaciones'

#view para eliminar un post
class EliminarPublicacionView(DeleteView):
    template_name='publicaciones/eliminar-publicacion.html'
    model = Publicacion
    success_url = '../ver-publicaciones'

#view para ver una publicacion
class VerPostView(DetailView):
    model=Publicacion
    template_name='publicaciones/ver-publicacion.html'
    context_object_name='publicacion'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context