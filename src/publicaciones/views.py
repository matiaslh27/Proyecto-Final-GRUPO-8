from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView

# Create your views here.
"""def publicaciones_view(request):
    ctx = {
        'publicaciones': Publicacion.objects.all(),
    }

    return render(request, 'publicaciones.html', ctx)

"""
#View hecha en clase para renderizar las publicaciones desde base de datos
class PublicacionesView(ListView):
    template_name = 'publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'