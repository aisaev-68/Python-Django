from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('bookapi.urls')),  # new
    path('admin/', admin.site.urls),
]
