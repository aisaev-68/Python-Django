from typing import List

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, View, DetailView, FormView
from .forms import PostForm, PostImageForm, SendMessageForm
from .models import Post, PostImage





class ShowBlogs(View):
    def get(self, request: HttpRequest, *args, **kwargs):
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


# class CreateBlog(CreateView):
#     form_class = PostForm
#     context_object_name = "post"
#     template_name = 'blogs/created_blog.html'

class CreateBlog(LoginRequiredMixin, View):
    # def get(self, request, *args, **kwargs):
    #     post_form = PostForm(instance=request.user)
    #     post = Post.objects.get_or_create(user_id=request.user.pk)[0]
    #     post_image_form = PostImageForm(instance=post)
    #
    #     context = {
    #         'post_form': post_form,
    #         'post_image_form': post_image_form
    #     }
    #
    #     return render(request, 'blogs/created_post.html', context)

    def post(self, request, *args, **kwargs):
        post_form = PostForm(
            request.POST,
            instance=request.user
        )
        post_image_form = PostImageForm(
            request.POST,
            request.FILES,
            instance=request.post
        )
        if post_form.is_valid() and post_image_form.is_valid():
            post_form.save()
            for file in request.FILES.getlist('image'):
                img = PostImage()
                img.post = post_form.cleaned_data['post']
                img.image =file
                img.save()

            return redirect('blogs:show_blogs')

        else:
            context = {
                'post_form': post_form,
                'post_image_form': post_image_form
            }
            messages.error(request, 'Ошибка обновления поста.')

            return render(request, 'accounts/profile.html', context)


class SendMessage(View):
    form_class = SendMessageForm
    template_name = "blogs/contact.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})