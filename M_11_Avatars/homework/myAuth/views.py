from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from . import forms
from .models import Profile


class MainPage(View):
    def get(self, request: HttpRequest):
        return render(request, 'myAuth/main.html')


class UsersList(ListView):
    template_name = 'myAuth/users-list.html'
    context_object_name = 'users'
    queryset = User.objects.select_related('profiles').all()


class AboutMe(DetailView):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['pk'])

        context = {
            'user': user,
        }

        return render(request, 'myAuth/about-me.html', context)


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm()
        profile_form = forms.ProfileForm()

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'myAuth/register.html', context)

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

            messages.success(request, 'Профиль создан.')
            user = authenticate(request, username=new_user, password=password)

            login(request, user)

            # return redirect('myAuth:about-me', pk=str(new_user.pk))
            return redirect(reverse('myAuth:about-me', kwargs={'pk': str(user.pk)}))


        else:

            messages.error(request, 'Ошибка создания профиля.')

            return render(request, 'myAuth/register.html', context)


class ProfileView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff or self.request.user.pk == self.kwargs['pk']

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['pk'])
        user_form = forms.UserFormUpdate(instance=user)
        profile = Profile.objects.get_or_create(user_id=user.pk)[0]
        profile_form = forms.ProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'myAuth/profile.html', context)

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

            messages.success(request, 'Профиль обновлен.')

            return redirect(reverse('myAuth:about-me', kwargs={'pk': str(user.pk)}))

        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            messages.error(request, 'Ошибка обновления профиля.')

            return render(request, 'myAuth/profile.html', context)
