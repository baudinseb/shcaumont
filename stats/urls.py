from django.conf.urls import patterns, url

from stats import views

urlpatterns = patterns('',
    url(r'^$', views.team, name='team'),
    url(r'^team/(\d+)/$', views.team_id, name='team'),
)