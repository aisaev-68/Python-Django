from django.urls import path

from .views import SignUpView, UserLogOut, UserLogIn, UserEditView, ShowProfilePageView


app_name = "accounts"
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("login/", UserLogIn.as_view(), name="login"),
    path("logout/", UserLogOut.as_view(), name="logout"),
    # path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    # path('edit_profile_page/<int:pk>/', EditProfilePageView.as_view(), name='edit_user_profile'),
    # path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
]