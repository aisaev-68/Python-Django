from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserFormUpdate(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя*',
            }
        ),
        required=True
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Фамилия*',
            }
        ),
        required=True
    )

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'placeholder': 'Email*',
        }
        ),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''
            self.fields[field].label = ''

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]


class UserForm(UserFormUpdate, forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Пользователь*',
            }
        ),
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Пароль*',
                'help_text': ''
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Повторный пароль*',
                'help_text': ''
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''
            self.fields[field].label = ''

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password no match')
        return cd['password1']

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', ]


class ProfileForm(forms.ModelForm):
    country = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Страна',
            }
        ),
        required=True
    )
    postal_code = forms.CharField(
        label='Почтовый индекс',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Почтовый индекс',
            }
        ),
        required=False
    )
    city = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Город',
            }
        ),
        required=False
    )
    address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Адрес',
            }
        ),
        required=False
    )

    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                'placeholder': 'Номер телефона*',
            },
        ),
        required=True
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'placeholder': 'Аватар',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = ''

    class Meta:
        model = Profile
        fields = ['avatar', 'country', 'postal_code', 'city', 'address', 'phone']
