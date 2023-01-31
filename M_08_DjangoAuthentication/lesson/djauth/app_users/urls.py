from django.urls import path
from django.shortcuts import render, redirect
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
]
