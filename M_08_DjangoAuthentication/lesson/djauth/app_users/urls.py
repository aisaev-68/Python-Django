from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("another_login/", views.UserLoginView.as_view(), name="another_login"),
    path("another_logout/", views.AnotherLogout.as_view(), name="another_logout"),
]
