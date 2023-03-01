from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from . import forms
from .models import Profile


class AboutMe(FormView):
    template_name = 'myAuth/about-me.html'
    form_class = forms.RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


class RegisterView(FormView):
    template_name = 'myAuth/register.html'
    form_class = forms.RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user_form = forms.UserUpdateForm(instance=request.user)
        profile = Profile.objects.get_or_create(user_id=request.user.pk)[0]
        profile_form = forms.ProfileUpdateForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'myAuth/profile.html', context)

    def post(self, request, *args, **kwargs):

        user_form = forms.UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = forms.ProfileUpdateForm(
            request.POST,
            # request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Профиль обновлен.')

            return redirect('myAuth:about-me')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, 'Ошибка обновления профиля.')

            return render(request, 'myAuth/profile.html', context)
