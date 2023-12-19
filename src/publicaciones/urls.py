from django.urls import path
from .views import  PublicacionesView



urlpatterns = [
    path('ver-publicaciones/', PublicacionesView.as_view(),name='posts')
]
    