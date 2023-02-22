from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile


class UserForm(forms.ModelForm):

    first_name = forms.CharField(
        label='Имя*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )
    last_name = forms.CharField(
        label='Фамилия*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )

    email = forms.EmailField(
        label="Email*",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]


class RegisterForm(UserCreationForm, forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя*',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
            }
        ),
        required=True
    )
    first_name = forms.CharField(
        label='Имя*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )
    last_name = forms.CharField(
        label='Фамилия*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )

    email = forms.EmailField(
        label="Email*",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        required=True
    )

    password1 = forms.CharField(
        label=_("Пароль*"),
        widget=forms.PasswordInput(),
        required=True
    )
    password2 = forms.CharField(
        label=_("Повторный пароль*"),
        widget=forms.PasswordInput(),
        required=True
    )

    country = forms.CharField(
        label='Страна*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )
    postal_code = forms.CharField(
        label='Почтовы индекс',
        widget=forms.TextInput(),
        required=False
    )
    city = forms.CharField(
        label='Город',
        max_length=200,
        widget=forms.TextInput(),
        required=False
    )
    address = forms.CharField(
        label='Адрес',
        max_length=200,
        widget=forms.TextInput(),
        required=False
    )

    phone = forms.CharField(
        label='Номер телефона*',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
            },
        ),
        required=True
    )
    avatar = forms.ImageField(
        label="Аватор профиля",
        required=False,
        widget=forms.FileInput()
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
        fields = 'avatar', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'country', 'postal_code', 'city', 'address', 'phone'


class ProfileForm(forms.ModelForm):
    country = forms.CharField(
        label='Страна*',
        max_length=100,
        widget=forms.TextInput(),
        required=True
    )
    postal_code = forms.CharField(
        label='Почтовы индекс',
        widget=forms.TextInput(),
        required=False
    )
    city = forms.CharField(
        label='Город',
        max_length=200,
        widget=forms.TextInput(),
        required=False
    )
    address = forms.CharField(
        label='Адрес',
        max_length=200,
        widget=forms.TextInput(),
        required=False
    )

    phone = forms.CharField(
        label='Номер телефона*',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
            },
        ),
        required=True
    )
    avatar = forms.ImageField(
        label="Аватор профиля",
        required=False,
        widget=forms.FileInput()
    )


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['avatar', 'country', 'postal_code', 'city', 'address', 'phone']


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
