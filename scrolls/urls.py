from django.conf.urls import url
from django.contrib import admin

from card_collection import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'collection/', views.card_collection, name='collection'),
    url(r'^$', views.index, name='index')
]
