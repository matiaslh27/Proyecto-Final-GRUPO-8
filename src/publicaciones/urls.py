from django.urls import path
from .views import  PublicacionesView, PostView, PostEditView



urlpatterns = [
    path('ver-publicaciones/', PublicacionesView.as_view(),name='posts'),
    path('crear-publicacion/', PostView.as_view(),name='crear-publicacion'),
    path('modify/<int:pk>', PostEditView.as_view(),name='modificar-publicacion'),
]
    