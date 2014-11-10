from django.conf.urls import patterns, include, url

from django.views.static import *
from django.conf import settings

from django.contrib.auth.views import login, logout
#from django.contrib.auth import login,logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^accounts/login/$', login),
    #url(r'^accounts/logout/$', logout),
    #url(r'^openid/', include('django_openid_auth.urls')),
    url(r'', include('start_page.urls')),
    #url(r'^start_page/', include('start_page.urls')),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^db_survey/', include('db_survey.urls', namespace="db_survey")),
    #url(r'^sa_stats/', include('sa_stats.urls', namespace="sa_stats")),
    url(r'^notify_configure_app/', include('notify_configure_app.urls', namespace="notify_configure_app")),
    #url(r'^sa_stats2/', include('sa_stats2.urls', namespace="sa_stats2")),
    #url(r'^nagios_aggregator/', include('nagios_aggregator.urls', namespace="nagios_aggregator")),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
