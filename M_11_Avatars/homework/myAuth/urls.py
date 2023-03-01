from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views

from .views import ProfileView, AboutMe, MainPage, UsersList, RegisterView

app_name = "myAuth"
urlpatterns = [
    path("", MainPage.as_view(), name="main_page"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("all/", UsersList.as_view(), name="users-list"),
    path("update/<int:pk>/", ProfileView.as_view(), name="user-update"),
    path("register/", RegisterView.as_view(), name="register"),
    path("about_me/<int:pk>/", AboutMe.as_view(), name="about-me"),

]