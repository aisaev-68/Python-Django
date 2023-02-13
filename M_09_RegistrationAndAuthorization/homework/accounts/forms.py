from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _
from .models import Profile


class RegisterUser(UserCreationForm, forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label=_("Повторный пароль"),
        widget=forms.PasswordInput(),
    )

    country = forms.CharField(
        label='Страна',
        max_length=100,
        widget=forms.TextInput(),
    )
    postal_code = forms.IntegerField(
        label='Почтовы индекс',
        min_value=1,
        widget=forms.NumberInput()
    )
    city = forms.CharField(
        label='Город',
        max_length=200,
        widget=forms.TextInput(),
    )
    address = forms.CharField(
        label='Адрес',
        max_length=200,
        widget=forms.TextInput(),
    )

    phone = forms.CharField(
        label='Номер телефона',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
            },
        ),
    )

    error_messages = {
        "password_mismatch": _("Пароли не совпадают!."),
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = 'username', 'email', 'password1', 'password2', 'country', 'postal_code', 'city', 'address', 'phone'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['country', 'postal_code', 'city', 'address', 'phone']



class UserRegistrationForm(UserCreationForm):
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
        fields = ('username', 'email', 'password1', 'password2')


class ProfileRegistrationForm(forms.ModelForm):

    country = forms.CharField(
        label='Страна', widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Страна',
                'help_text': ''
            }
        )
    )

    address = forms.CharField(
        label='Адрес', widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Адрес',
                'help_text': ''
            }
        )
    )

    phone = forms.CharField(
        label='Номер телефона', widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Номер телефона',
                'help_text': ''
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('country', 'address', 'phone')
