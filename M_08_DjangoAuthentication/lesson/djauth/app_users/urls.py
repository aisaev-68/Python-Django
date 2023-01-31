from django.urls import path
from django.shortcuts import render, redirect
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("another_login/", views.UserLoginViev.as_view, name="another_login"),
]
