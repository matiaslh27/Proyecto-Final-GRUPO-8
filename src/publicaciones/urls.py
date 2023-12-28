from django.urls import path
from .views import  PublicacionesView, PostView, PostEditView , EliminarPublicacionView, VerPostView, EliminarComentarioView



urlpatterns = [
    path('ver-publicaciones/', PublicacionesView.as_view(),name='posts'),
    path('crear-publicacion/', PostView.as_view(),name='crear-publicacion'),
    path('modify/<int:pk>', PostEditView.as_view(),name='modificar-publicacion'),
    path('eliminar/<int:pk>', EliminarPublicacionView.as_view(),name='eliminar-publicacion'),
    path('detalle/<int:pk>',VerPostView.as_view(),name='ver-publicacion'),
    path('eliminar-comentario/<int:pk>',EliminarComentarioView.as_view(), name='eliminar-comentario')
]
    