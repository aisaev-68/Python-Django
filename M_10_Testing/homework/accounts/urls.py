from django.urls import path
from django.contrib.auth import views

from .views import ProfileView, AboutMe

app_name = "myAuth"
urlpatterns = [
    path("update/", ProfileView.as_view(), name="profile"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("about_me/<int:pk>/", AboutMe.as_view(), name="about-me"),
]
