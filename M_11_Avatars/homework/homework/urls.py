from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from myAuth.views import RegisterView

urlpatterns = [
    # path('', RedirectView.as_view(url='/', permanent=True)),
    path('admin/', admin.site.urls),
    path('', include('myAuth.urls'), name="myAuth"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
