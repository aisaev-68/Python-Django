from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
]
