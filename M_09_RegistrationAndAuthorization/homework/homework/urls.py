from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import RegisterView

urlpatterns = [
    path('', RedirectView.as_view(url='/shopapp/', permanent=True)),
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('myAuth/', include('django.contrib.auth.urls'), name="myAuth"),
    path('profile/', include('myAuth.urls'), name="myAuth"),
    path('shopapp/', include('shopapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
