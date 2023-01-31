from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("another_login/", views.UserLoginView.as_view(), name="another_login"),
]
