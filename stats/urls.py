from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^$', views.team, name='team'),
    url(r'^team/(\d+)/$', views.team_id, name='team_id'),
    url(r'^player/(\d+)/$', views.player_id, name='player_id'),
    url(r'^player/record/(\d+)/$', views.record_player_id, name='record_player_id'),
)