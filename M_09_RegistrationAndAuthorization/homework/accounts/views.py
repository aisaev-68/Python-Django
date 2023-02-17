from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from . import forms
from .models import Profile


class Register(CreateView):
    form_class = forms.RegisterUser
    template_name = 'accounts/register.html'

    def get_success_url(self):
        return reverse(
            'login',
            # kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        country = form.cleaned_data.get("country")
        postal_code = form.cleaned_data.get("postal_code")
        city = form.cleaned_data.get("city")
        address = form.cleaned_data.get("address")
        phone = form.cleaned_data.get("phone")
        Profile.objects.create(user=self.object, country=country, postal_code=postal_code, city=city, address=address, phone=phone)
        # user = authenticate(
        #     self.request,
        #     username=username,
        #     password=password
        # )
        # login(request=self.request, user=user)
        return response





class ProfileDetail(TemplateView):
    template_name = 'accounts/about-me.html'

    def get_success_url(self):
        return reverse(
            "accounts:profile",
            kwargs={"pk": self.object.pk},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = User.objects.get(pk=self.kwargs['pk'])
        context['user'] = user
        # context['profile'] = Profile.objects.get(user_id=user.pk)
        context['profile'] = get_object_or_404(Profile, user_id=user.pk)
        return context


class ProfileUpdate(UpdateView):
    form_class = forms.ProfileForm
    template_name = 'accounts/update_profile.html'


    def get_queryset(self):
        queryset = Profile.objects.filter(pk=self.kwargs['pk'])
        return queryset
    #
    def get_success_url(self):
        return reverse(
            "accounts:profile",
            kwargs={"pk": self.object.user.pk},
        )


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     profile = Profile.objects.get(user=self.kwargs['pk'])
    #     print(9999, profile)
    #     user = User.objects.get(pk=profile.user.pk)
    #     print(1000, user)
    #
    #     context['user_form'] = forms.UserForm(instance=user)
    #     context['profile_form'] = forms.ProfileForm(instance=profile)
    #     return context






