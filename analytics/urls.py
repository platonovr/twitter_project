from django.conf.urls import url, patterns
from django.views.generic import TemplateView, DetailView, ListView
from twitter.models import Tweet

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name="analytics/index.html"), name="index"),
                       url(r'^tweet/(?P<pk>\d+)',
                           DetailView.as_view(model=Tweet, template_name="analytics/tweet_detail.html")),
                       url(
                           r'^tweets/',
                           ListView.as_view(model=Tweet, template_name="analytics/tweet_list.html", paginate_by=3)
                       ),
)
