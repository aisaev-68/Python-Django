from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    # path('', lambda req: redirect('/login/')),
    path('users/', include('app_users.urls')),
]
