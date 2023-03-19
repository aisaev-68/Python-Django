from typing import List

from django.contrib.auth.models import User
from django.forms import HiddenInput, modelformset_factory
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View, DetailView, FormView
from .forms import PostForm, PostImageForm, SendMessageForm
from .models import Post, PostImage


class ShowBlogs(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        print(7777777777)
        user_id = self.kwargs.get('pk')

        if user_id:
            posts = [p for p in Post.objects.filter(created_by_id=user_id)]
            context = {
                "posts": posts
            }
        else:
            posts = [p for p in Post.objects.all()]
            context = {
                'posts': posts
            }

        return render(request, 'blogs/blogs_list.html', context=context)


class BlogDetail(DetailView):
    model = PostImage
    context_object_name = "posts"
    template_name = 'blogs/blogs_detail.html'

    def get_object(self, queryset=None):
        queryset = Post.objects.filter(pk=self.kwargs['pk'])
        return super().get_object(queryset)


@login_required
def create_blog(request: HttpRequest):
    ImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=3)
    if request.method == "POST":
        post_form = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())

        if post_form.is_valid() and formset.is_valid():
            new_post = Post(created_by=request.user)
            new_post.title = post_form.cleaned_data['title']
            new_post.description = post_form.cleaned_data['description']
            print(8888888, new_post.pk, request.user.pk)
            # new_post.create_by = request.user.pk
            new_post.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['images']
                    photo = PostImage(post=new_post, image=image)
                    photo.save()
            messages.success(request, "Posted!")
            return redirect('blogs:show_blogs')
        else:
            print(post_form.errors, formset.errors)
    else:
        post_form = PostForm()
        formset = ImageFormSet(queryset=PostImage.objects.none())

    return render(request, 'blogs/created_post.html', context={'form': post_form, 'formset': formset})


class SendMessage(View):
    form_class = SendMessageForm
    template_name = "blogs/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})


class BlogerProfile(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'blogs/bloger_profile.html', context={"user": user})