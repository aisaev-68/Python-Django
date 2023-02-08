from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from . import forms
from news_site.models import Profile



class SignUpView(CreateView):
    model = Profile
    form_class = forms.ProfileForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'news_site/signup.html'
    success_msg = 'Пользователь успешно создан'

    # def get_success_url(self):
    #     return reverse('accounts:login', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = forms.LoginForm(instance=self.request.user)
        return context




class UserLogIn(LoginView):
    form_class = forms.LoginForm
    template_name = "news_site/login.html"
    fields = ["username", "password"]




# class UserLogOut(LogoutView):
#     next_page = '/news_site/'

class UserLogOut(LoginRequiredMixin, LogoutView):
    template_name = 'news_site/logout.html'