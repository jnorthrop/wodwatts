from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'application.views.index'),
	url(r'^(?P<user_id>\d+)/$', 'application.views.session'),
	url(r'^(?P<user_id>\d+)/(?P<session_id>\d+)/$', 'application.views.exercise'),
   url(r'^admin/', include(admin.site.urls)),
)
