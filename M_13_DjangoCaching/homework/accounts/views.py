from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from . import forms
from .models import Profile


class AboutMe(LoginRequiredMixin, DetailView):

    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user)
        profile = Profile.objects.get_or_create(user_id=request.user.pk)[0]
        profile_form = forms.ProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'accounts/about-me.html', context)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm()
        profile_form = forms.ProfileForm()

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'accounts/register.html', context)

    def post(self, request, *args, **kwargs):
        user_form = forms.UserForm(
            request.POST,
        )

        profile_form = forms.ProfileForm(
            request.POST,
            request.FILES,

        )
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            password = user_form.cleaned_data['password1']
            new_user.set_password(password)
            new_user.save()

            profile.user = new_user
            profile.avatar = request.FILES.get('avatar')
            profile.save()

            client_group = Group.objects.get(name="Clients")
            new_user.groups.add(client_group)
            messages.success(request, _('Created profile.'))
            user = authenticate(request, username=new_user, password=password)

            login(request, user)

            return redirect(reverse('accounts:about-me', kwargs={'pk': str(user.pk)}))


        else:

            messages.error(request, _('Profile creation error.'))

            return render(request, 'accounts/register.html', context)


class ProfileView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_form = forms.UserFormUpdate(instance=request.user)
        profile = Profile.objects.get_or_create(user_id=request.user.pk)[0]
        profile_form = forms.ProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'accounts/profile.html', context)

    def post(self, request, *args, **kwargs):

        user_form = forms.UserFormUpdate(
            request.POST,
            instance=request.user
        )

        profile_form = forms.ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profiles
        )

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            user.save()
            profile.save()

            messages.success(request, _('Update profile.'))

            return redirect(reverse('accounts:about-me', kwargs={'pk': str(user.pk)}))

        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, _('Profile update error.'))

            return render(request, 'accounts/profile.html', context)
