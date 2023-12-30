from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404,redirect
from .models import Publicacion, Comentario, Categoria
from .forms import PostForm,ComentarioForm
from django.views.generic import ListView , CreateView , UpdateView , DeleteView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import ColaboradorMixin, CreadorMixin

# Create your views here.
"""def publicaciones_view(request):


    return render(request, 'publicaciones/publicaciones.html', {'publicaciones': Publicacion.objects.all(),})

"""
#View hecha en clase para renderizar las publicaciones desde base de datos
class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        #filtrando x categoria
        categoria_seleccionada = self.request.GET.get('categoria')

        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)

        #Orden
        orden = self.request.GET.get('orderby')
        if orden:
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')
        return queryset


#View para publicar
class PostView(LoginRequiredMixin,ColaboradorMixin,CreateView):
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
class PostEditView(LoginRequiredMixin,CreadorMixin,UpdateView):
    template_name='publicaciones/modificar-publicacion.html'
    model = Publicacion
    form_class = PostForm
    success_url = '../ver-publicaciones'

#view para eliminar un post
class EliminarPublicacionView(LoginRequiredMixin,CreadorMixin,DeleteView):
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
    
    def post(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return redirect('login')
        
        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario= form.save(commit=False)
            comentario.creador_id=self.request.user.id
            comentario.publicacion=publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)
        
class EliminarComentarioView(LoginRequiredMixin,CreadorMixin,DeleteView):
    template_name='comentarios/eliminar-comentario.html'
    model=Comentario
    
    def get_success_url(self):
        return reverse ('ver-publicacion', args=[self.object.publicacion.id])

class EditarComentarioView(LoginRequiredMixin, CreadorMixin,UpdateView):
    template_name='comentarios/editar-comentario.html'
    model=Comentario
    form_class=ComentarioForm

    def get_success_url(self):
        return reverse ('ver-publicacion', args=[self.object.publicacion.id])

def me_gusta(request):
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        publicacion = get_object_or_404(Publicacion, id=publicacion_id)
        user = request.user

        if publicacion.me_gusta.filter(id=user.id).exists():
            publicacion.me_gusta.remove(user)
        else:
            publicacion.me_gusta.add(user)
        
    return redirect('posts')