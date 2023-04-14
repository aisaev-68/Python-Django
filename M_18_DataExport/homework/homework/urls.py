from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
# import debug_toolbar
from drf_yasg.views import get_schema_view
# from drf_yasg.views import get_schema_view
from rest_framework import permissions
from houseroom.sitemaps import HouseRoomSitemap, NewsSitemap

from houseroom.views import Contact, About

schema_view = get_schema_view(
   openapi.Info(
      title="House Room API",
      default_version='v1',
      description="Project Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="aisaev-68@yandex.ru"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

sitemaps = {
    # 'about': AboutSitemap,
    'news_detail': NewsSitemap,
    'houses': HouseRoomSitemap,
    }

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', RedirectView.as_view(url='/houseroom/', permanent=True)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('api.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    path('houseroom/', include('houseroom.urls'), name="houseroom"),
    path('news/', include('news.urls'), name="news"),
    path('rss/', include('news_rss.urls'), name="news-rss"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
