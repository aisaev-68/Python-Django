from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from accounts.views import Register

urlpatterns = [
    path('', RedirectView.as_view(url='/shopapp/', permanent=True)),
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls'), name="accounts"),
    path('profile/', include('accounts.urls'), name="accounts"),
    path('shopapp/', include('shopapp.urls')),
]
