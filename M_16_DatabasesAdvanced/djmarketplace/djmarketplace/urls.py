from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from app_users.views import RegisterView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    # path('', RedirectView.as_view(url='/shopapp/', permanent=True)),
    path('admin/', admin.site.urls),
    # path('register/', RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls'), name="accounts"),
    # path('profile/', include('accounts.urls'), name="accounts"),
    # path('shopapp/', include('shopapp.urls')),
    # path('blogs/', include('blogs.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
