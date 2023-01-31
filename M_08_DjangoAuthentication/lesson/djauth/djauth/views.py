from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse

from django.views import View
class MainView(View):
    def get(self, request: HttpRequest):
        return render(request, 'app_users/main.html')