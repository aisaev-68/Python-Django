from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

class MainPageView(View):
    def get(self, request: HttpRequest):
        if request.COOKIES.get("sessionid", None):
            return render(request, 'shopapp/shop.html')
        else:
            return render(request, 'shopapp/main.html')
