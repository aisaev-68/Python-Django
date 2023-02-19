from django.forms.models import ModelForm
from django import forms
from .models import Post, PostImage


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].help_text = ''

    class Meta:
        model = Post
        fields = ["title", "description", ]


class PostImageForm(ModelForm):
    image = forms.ImageField(
        label="Изображение",
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = PostImage
        fields = ["image", ]