from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from .forms import SignUpForm
from django.contrib.auth import login


# Create your views here.


class SignUpView(CreateView):
    model=User
    template_name='users/registrarse.html'   
    form_class= SignUpForm

    def form_valid(self, form):
        """redefiniendo el metodo form_valid para que inicie la sesion al registrarse"""
        response= super().form_valid(form)
        user = form.save()
        login(self.request,user)
        return response

    
 