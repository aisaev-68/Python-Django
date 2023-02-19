from typing import List

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, View
from .forms import PostForm, PostImageForm
from .models import Post, PostImage





class ShowBlogs(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        user_id = self.kwargs.get('pk')

        if user_id:
            post = Post.objects.filter(created_by_id=user_id)
            context = {"posts": Post.objects.filter(created_by=user_id)}
        else:
            # posts = Post.objects.all()
            # print(9999, [p.pk for p in Post.objects.all()])
            # posts_id = [p.pk for p in posts]
            post_img = PostImage.objects.select_related("post").all()
            print(8888, [p.to_json() for p in post_img])
            context = {"posts": PostImage.objects.all()}

        return render(request, 'blogs/blogs_list.html', context=context)


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