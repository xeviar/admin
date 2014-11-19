from django.conf.urls import patterns, url, include
#from django.contrib.auth.views import login, logout

from start_page import views

urlpatterns = patterns('', 
#url('', include('social.apps.django_app.urls', namespace='social')),
url(r'^$', views.start_page),
url(r'^logout$', views.log_out),
url(r'^product/(\w+)/$', views.product),
url(r'^getstatus/(\w+)/(\w+)/$', views.getstatus),
url(r'^getdetail/(\w+)/(\w+)/$', views.getdetail),
url(r'^test/$', views.test),
url(r'^test/(\w+)/$', views.test),
)
