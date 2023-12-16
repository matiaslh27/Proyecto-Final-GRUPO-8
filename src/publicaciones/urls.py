from django.urls import path
from .views import publicaciones_view



urlpatterns = [
    path('ver-publicaciones/', publicaciones_view,name='posts')
]
    