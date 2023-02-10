from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from . import forms
from news_site.models import Profile


class SignUpView(CreateView):
    form_class = forms.SignUpForm
    # success_url = reverse_lazy('accounts:user_profile')
    template_name = 'news_site/signup.html'
    success_msg = 'Пользователь успешно создан'

    def get_success_url(self):
        return reverse(
            'accounts:user_profile',
            kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        print(888, response)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        phone = form.cleaned_data.get("phone")
        city = form.cleaned_data.get("city")
        pk = Profile.objects.create(user=self.object, phone=phone, city=city)
        print(666666, pk)
        self.object = pk
        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)
        return response



class UserLogIn(LoginView):
    form_class = forms.LoginForm
    template_name = "news_site/login.html"
    fields = ["username", "password"]


class UserLogOut(LoginRequiredMixin, LogoutView):
    template_name = 'news_site/logout.html'


class UserEditView(UpdateView):
    form_class = forms.EditProfileForm
    template_name = 'news_site/edit_profile.html'
    # success_url = reverse_lazy('accounts:user_profile')

    def get_success_url(self):
        print(222, self.object.pk)
        return reverse(
            'accounts:user_profile',
            kwargs={"pk": self.object.pk},
        )

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = forms.UserEditForm(instance=self.request.user)
    #     context['user_form'] = forms.EditProfileForm(instance=self.request.profile)
    #     return context

    def form_valid(self, form):
        form = super().form_valid(form)
        form.save()
        return form

    def get_object(self):
        return self.request.user


class ShowProfilePageView(DetailView):

    model = Profile
    context_object_name = "profiles"
    template_name = 'news_site/user_profile.html'
    # queryset = Profile.objects.select_related("user").all()


