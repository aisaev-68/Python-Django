from django.urls import path

from .views import SignUpView, UserLogOut, UserLogIn


app_name = "accounts"
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("login/", UserLogIn.as_view(), name="login"),
    path("logout/", UserLogOut.as_view(), name="logout"),
]