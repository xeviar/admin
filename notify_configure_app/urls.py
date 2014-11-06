from django.conf.urls import patterns, url
#from django.contrib.auth.views import login, logout

#from polls import views
from notify_configure_app import views

urlpatterns = patterns('',
url(r'^view_existing$', views.view_existing),
url(r'^submit$', views.submit),
#url(r'^accounts/login/$', login),
#url(r'^accounts/profile/$', views.sms_stats),
#url(r'^accounts/logout/$', logout),
)
