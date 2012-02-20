from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'application.views.index', name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.urls')),
	url(r'^profile/', 'application.views.profile'),
	url(r'^session/$', 'application.views.session'),
	url(r'^session/(?P<session_id>\d+)/$', 'application.views.session'),
	url(r'^session/(?P<session_id>\d+)/exercise/$', 'application.views.exercise'),
	url(r'^session/(?P<session_id>\d+)/exercise/(?P<exercise_id>\d+)/$', 'application.views.exercise'),
)