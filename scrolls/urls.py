from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from card_collection import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'cards/$', views.CardList.as_view(), name='cards'),
    url(r'^(?P<pk>[0-9]+)$', views.CardDetails.as_view(), name='card_details'),
    url(r'^$', views.Index.as_view(), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

