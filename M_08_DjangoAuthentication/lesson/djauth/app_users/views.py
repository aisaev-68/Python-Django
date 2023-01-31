import datetime

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm

# def home(request: HttpRequest):
#     # return redirect(reverse('app_users/login.html'))
#     return redirect(reverse('app_users/login.html'))


class UserLoginViev(LoginView):
    template_name = "app_users/login.html"


def time_in_range(current_time: datetime):
    start = datetime.time(0, 0, 0)
    end = datetime.time(22, 0, 0)
    current = datetime.datetime.now().time()

    return start <= current <= end


def user_login(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            current_time = datetime.datetime.now().time()
            if user is not None:
                if not user.is_superuser:
                    if time_in_range(current_time):
                        if user.is_active:
                            login(request, user)
                            return HttpResponse('Аутентификация выполнена успешно.')
                        else:
                            return HttpResponse('Аккаунт не активен.')
                    else:
                        return HttpResponse('Доступ к аккаунту ограничен с 22ч по 8ч.')
                else:
                    return HttpResponse('Доступ администратору запрещен.')
            else:
                return HttpResponse('Аккаунт с таким логином или паролем отсуствует.')
    else:
        form = LoginForm()
    return render(request, 'app_users/login.html', {'form': form})
