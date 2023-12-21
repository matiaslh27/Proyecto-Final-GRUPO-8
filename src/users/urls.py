from django.urls import path
from .views import  SignUpView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('crear-usuario/', SignUpView.as_view(),name='registrarse'),
    path('login/', LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout')
]