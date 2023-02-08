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

from .models import Profile, Article



class NewsList(ListView):
    # model = Article
    context_object_name = "articles"
    template_name = 'news_site/articles_list.html'
    queryset = Article.objects.all()


class NewsCreate(CreateView):
    model = Article
    template_name = 'news_site/create_news.html'
    fields = ["title", "content"]
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


        return form
