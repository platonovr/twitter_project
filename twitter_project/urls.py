from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'twitter.views.index', name='index'),
                       url(r'^process/$', 'twitter.views.process', name='process'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
)
