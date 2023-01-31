import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views import View

def time_in_range(current_time: datetime):
    start = datetime.time(8, 0, 0)
    end = datetime.time(22, 0, 0)
    current = datetime.datetime.now().time()

    return start <= current <= end


class MainView(View):
    def get(self, request: HttpRequest):
        current_time = datetime.datetime.now().time()
        if time_in_range(current_time):
            if request.COOKIES.get("sessionid", None):
                return render(request, 'app_users/first_page.html')
            else:
                return render(request, 'app_users/main.html')
        else:
            return HttpResponse('Доступ к аккаунту ограничен с 22ч по 8ч.')