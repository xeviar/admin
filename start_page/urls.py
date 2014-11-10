from django.conf.urls import patterns, url
#from django.contrib.auth.views import login, logout

#from polls import views
from start_page import views

urlpatterns = patterns('', 
#url(r'^accounts/profile/$', views.sms_stats),
url(r'^$', views.start_page),
url(r'^test/$', views.test),
url(r'^test/(\w+)/$', views.test),
)
