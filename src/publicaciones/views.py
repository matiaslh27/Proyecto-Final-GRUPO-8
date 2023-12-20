from django.shortcuts import render
from .models import Publicacion
from .forms import PostForm
from django.views.generic import ListView , CreateView , UpdateView , DeleteView

# Create your views here.
"""def publicaciones_view(request):


    return render(request, 'publicaciones/publicaciones.html', {'publicaciones': Publicacion.objects.all(),})

"""
#View hecha en clase para renderizar las publicaciones desde base de datos
class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'

class Publicar(CreateView):
    template_name='publicaciones/publicar.html'
    model = Publicacion
    form_class = PostForm
