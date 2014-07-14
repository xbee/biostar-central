from __future__ import (unicode_literals, division, absolute_import)
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.TorrentList.as_view(), name='index'),
    url(r'^peers/$', views.PeerList.as_view(), name='peer-list'),
    #url(r'^upload/$', views.TorrentUploadView.as_view(), name='upload'),
    url(r'^download/(?P<pk>\d+)/$', views.download_torrent, name='download'),
    url(r'^view/peer/(?P<pk>\d+)/$', views.PeerDetail.as_view(), name='view-peer'),
    url(r'^view/torrent/(?P<pk>\d+)/$', views.TorrentDetail.as_view(), name='view-torrent'),
    url(r'^announce$', views.announce, name='announce'),
    url(r'^scrape$', views.scrape, name='scrape'),
)