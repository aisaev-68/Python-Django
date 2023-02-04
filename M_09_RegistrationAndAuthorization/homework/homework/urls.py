from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/news_site/', permanent=True)),
    path('admin/', admin.site.urls),
    path('news_site/', include('news_site.urls')),
]