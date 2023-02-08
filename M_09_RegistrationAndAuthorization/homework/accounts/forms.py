from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from news_site.models import Profile




class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    error_messages = {
        "invalid_login": _(
            "Пожалуйста, введите правильный %(username)s и пароль. Обратите внимание, что оба "
             "поля могут быть чувствительны к регистру."
        ),
        "inactive": _("Этот аккаунт не активен."),
    }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'city']

