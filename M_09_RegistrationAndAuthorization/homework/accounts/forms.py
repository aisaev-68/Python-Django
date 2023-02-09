from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from news_site.models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    error_messages = {
        "invalid_login": _(
            "Пожалуйста, введите правильный %(username)s и пароль. Обратите внимание, что оба "
            "поля могут быть чувствительны к регистру."
        ),
        "inactive": _("Этот аккаунт не активен."),
    }


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Пользователь', widget=forms.TextInput(
            attrs={
                "autofocus": True,
                'class': 'form-input',
                'placeholder': 'Пользователь',
                'help_text': ''
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Пароль',
                'help_text': ''
            }
        )
    )
    password2 = forms.CharField(
        label='Повторный пароль', widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Повторный пароль',
                'help_text': ''
            }
        )
    )
    error_messages = {
        "password_mismatch": _("Пароли не совпадают!."),
    }

    class Meta:
        model = User
        fields = 'username', 'password1', 'password2'


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'city']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер телефона'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Город'}),
        }
