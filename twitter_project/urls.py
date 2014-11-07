from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('twitter.views',
                       # Examples:
                       url(r'^$', 'index', name='index'),
                       url(r'^process/$', 'process', name='process'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^signin/', 'sign_in', name='sign_in'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^q/$', 'q', name='q'),
                       url(r'^signout/', 'sign_out', name='sign_out'),
                       url(r'^analytics/', include('analytics.urls', namespace='analytics')),
)
