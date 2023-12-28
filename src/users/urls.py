from django.urls import path
from .views import  SignUpView, ver_perfil_view, EditarPerfilView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('crear-usuario/', SignUpView.as_view(),name='registrarse'),
    path('login/', LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('ver-perfil/',ver_perfil_view,name='ver-perfil'),
    path('editar-perfil/<int:pk>',EditarPerfilView.as_view(),name='editar-perfil'),
]