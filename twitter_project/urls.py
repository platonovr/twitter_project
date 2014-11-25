from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter.views import UserTweetListView, LoginView
from twitter_project import settings

urlpatterns = patterns('twitter.views',
                       # Examples:
                       url(r'^$', UserTweetListView.as_view(), name='index'),
                       url(r'^process/$', 'process', name='process'),
                       url(r'^page(?P<page>\d+)$', UserTweetListView.as_view(), name='index'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^signin/', LoginView.as_view(), name='sign_in'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^q/$', 'q', name='q'),
                       url(r'^signout/', 'sign_out', name='sign_out'),
                       url(r'^analytics/', include('analytics.urls', namespace='analytics')),
                       url(r'^edit/$', 'edit_avatar', name='edit_avatar'),
                       url(r'^get_users/$', 'get_users', name='get_users'),
)

urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}),
)
