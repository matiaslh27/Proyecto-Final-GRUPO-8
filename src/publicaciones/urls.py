from django.urls import path
from .views import  PublicacionesView, Publicar



urlpatterns = [
    path('ver-publicaciones/', PublicacionesView.as_view(),name='posts'),
    path('crear-publicacion/', Publicar.as_view(),name='crear-publicacion')
]
    