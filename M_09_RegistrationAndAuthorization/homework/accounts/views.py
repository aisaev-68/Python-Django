from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class SignUpView(CreateView):
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserLogIn(LoginView):
    form_class = forms.LoginForm
    # template_name = "news_site/login.html"
    fields = ["username", "password"]




class UserLogOut(LogoutView):
    next_page = '/news_site/'