from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.urls')),
)