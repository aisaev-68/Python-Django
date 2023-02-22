from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView
from django.views.generic import FormView
from . import forms
from .models import Profile


class AboutMe(DetailView):
    # template_name = 'accounts/about-me.html'
    # form_class = forms.RegisterForm
    # redirect_authenticated_user = True
    # success_url = reverse_lazy('tasks')

    def get(self, request, *args, **kwargs):
        print(66666, self.kwargs['pk'])
        user_form = forms.UserForm(instance=request.user)
        profile = Profile.objects.get(user_id=self.kwargs['pk'])
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
            instance=request.user
        )

        profile_form = forms.ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profiles
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Профиль создан.')

            return redirect('accounts:about-me')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, 'Ошибка создания профиля.')

            return render(request, 'accounts/register.html', context)


class ProfileView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user)
        profile = Profile.objects.get_or_create(user_id=request.user.pk)[0]
        profile_form = forms.ProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'accounts/profile.html', context)

    def post(self, request, *args, **kwargs):

        user_form = forms.UserForm(
            request.POST,
            instance=request.user
        )

        profile_form = forms.ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profiles
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Профиль обновлен.')

            return redirect(reverse('accounts:about-me'))
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, 'Ошибка обновления профиля.')

            return render(request, 'accounts/profile.html', context)
