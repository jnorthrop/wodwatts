from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'placeholder.views.index', name='index'),
   # url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'placeholder.html'}),
   url(r'^admin/', include(admin.site.urls)),
)
