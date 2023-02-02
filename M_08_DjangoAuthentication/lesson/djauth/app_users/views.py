from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator


from .forms import LoginForm

# def home(request: HttpRequest):
#     # return redirect(reverse('app_users/login.html'))
#     return redirect(reverse('app_users/login.html'))


def logout_view(request: HttpRequest):
    logout(request)
    # return HttpResponse('Вы успешно вышли из под своей учетной записи.')
    return render(request, 'app_users/main.html')



def user_login(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if not user.is_superuser:
                    if user.is_active:
                        login(request, user)
                        # return HttpResponse('Аутентификация выполнена успешно.')
                        return render(request, 'app_users/first_page.html')
                    else:
                        return HttpResponse('Аккаунт не активен.')

                else:
                    return HttpResponse('Доступ администратору запрещен.')
            else:
                return HttpResponse('Аккаунт с таким логином или паролем отсуствует.')
    else:
        form = LoginForm()
    return render(request, 'app_users/login.html', {'form': form})


class UserLoginView(LoginView):
    template_name = "app_users/login.html"


class AnotherLogout(LogoutView):
    # template_name = "app_users/main.html"
    next_page = '/'