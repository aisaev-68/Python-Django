from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate
from django.forms import Form, HiddenInput
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

from .models import UserProfile, Article



class UserRegisterProfile(CreateView):
    model = UserProfile
    context_object_name = "register"
    template_name = 'news_site/create_profile.html'
    fields = ["user", "phone", "city", "verification_flag", "count_news"]
    # success_url = reverse_lazy("news_site:products_list")



    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['user'].widget.attrs.update({'class': 'user_name'})
        form.fields['phone'].widget.attrs.update({'class': 'phone_user'})
        form.fields['city'].widget.attrs.update({'class': 'city'})
        form.fields['verification_flag'].widget.attrs.update({'class': 'verification_flag'})
        form.fields['count_news'].widget.attrs.update({'class': 'count_news'})
        form.fields['count_news'].widget.attrs['min'] = 0
        return form

    # def get_context_data(self, *args, **kwargs):
    #     users = UserProfile.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
    #     context['page_user'] = page_user
    #     return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('tasks')





class NewsList(ListView):
    # model = Article
    # context_object_name = "news_list"
    template_name = 'news_site/articles_list.html'
    queryset = Article.objects.all()


class NewsCreate(CreateView):
    model = Article
    template_name = 'news_site/create_news.html'
    fields = ["pk", "title", "content", "published", "modified", "author"]
    success_url = reverse_lazy("news_site:news_list")

    def get_initial(self):
        return {'user': self.request.user}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({'class': 'title_article'})
        form.fields['content'].widget.attrs.update({'class': 'content_article'})
        form.fields['published'].widget.attrs.update({'class': 'content_published'})
        form.fields['modified'].widget.attrs.update({'class': 'content_modified'})
        form.fields['author'].widget.attrs.update({'class': 'author'})
        form.fields['author'].widget = HiddenInput()

        return form
