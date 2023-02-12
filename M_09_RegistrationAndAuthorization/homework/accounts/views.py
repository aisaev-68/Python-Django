from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from . import forms
from shopapp.models import Profile


class Register(CreateView):
    form_class = forms.RegisterUser
    template_name = 'shopapp/register.html'

    def get_success_url(self):
        return reverse(
            'login',
            # kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        phone = form.cleaned_data.get("phone")
        city = form.cleaned_data.get("city")
        Profile.objects.create(user=self.object, phone=phone, city=city)
        # user = authenticate(
        #     self.request,
        #     username=username,
        #     password=password
        # )
        # login(request=self.request, user=user)
        return response





class ProfileDetail(TemplateView):
    template_name = 'shopapp/about-me.html'

    def get_success_url(self):
        return reverse(
            "accounts:update_profile",
            kwargs={"pk": self.object.pk},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = User.objects.get(pk=self.kwargs['pk'])
        context['user'] = user
        context['profile'] = Profile.objects.get(user_id=user.pk)
        return context


class ProfileUpdate(UpdateView):
    form_class = forms.ProfileForm
    template_name = 'shopapp/update_profile.html'
    # success_url = 'accounts:profile'
    # fields = '__all__'

    def get_queryset(self):
        queryset = Profile.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def get_success_url(self):
        return reverse(
            "accounts:profile",
            kwargs={"pk": self.kwargs['pk']},
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


class ProfileDelete(DeleteView):
    model = Profile
    context_object_name = "profile"
    template_name = 'shopapp/delete_profile.html'


