from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from .forms import SignUpForm



# Create your views here.


class SignUpView(CreateView):
    model=User
    template_name='users/registrarse.html'   
    form_class= SignUpForm
    
