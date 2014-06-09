# codig: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('subscriptions.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)
