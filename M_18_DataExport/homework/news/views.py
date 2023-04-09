from django.shortcuts import render
from django.views import View

from news.models import News


class NewsView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "news": News.objects.all()
        }
        return render(request, "houseroom/news.html", context=context)