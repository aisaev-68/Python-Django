from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from news.models import News



class NewsDetail(DetailView):
    model = News
    template_name = 'houseroom/news_detail.html'


class NewsView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "news": News.objects.all()
        }
        return render(request, "houseroom/news.html", context=context)