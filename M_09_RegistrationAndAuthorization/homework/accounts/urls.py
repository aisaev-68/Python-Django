from django.urls import path
from django.contrib.auth import views

from .views import ProfileDetail, ProfileUpdate

app_name = "accounts"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("user/<int:pk>/", ProfileDetail.as_view(), name="profile"),
    path("update/<int:pk>/", ProfileUpdate.as_view(), name="update_profile"),

    # path("login/", UserLogIn.as_view(), name="login_page"),
    # path("logout/", UserLogOut.as_view(), name="logout_page"),
    # path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('user_profile/create/', ShowProfilePageView.as_view(), name='create_profile'),
    # path('edit_profile_page/<int:pk>/', EditProfilePageView.as_view(), name='edit_user_profile'),
    # path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
]
