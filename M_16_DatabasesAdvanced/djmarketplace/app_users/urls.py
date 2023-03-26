from django.urls import path
from django.contrib.auth import views

from app_users.views import RegisterView, AboutMe, ProfileView, UserLogin

name = 'app_users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("update/", ProfileView.as_view(), name="profile"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="shopapp/shop-list.html"), name="logout"),
    path("about_me/<int:pk>/", AboutMe.as_view(), name="about-me"),
]
