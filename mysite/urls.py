from django.conf.urls import patterns, include, url

from django.views.static import *
from django.conf import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('start_page.urls')),
    url(r'^start_page/', include('start_page.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
