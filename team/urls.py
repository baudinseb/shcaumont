from django.conf.urls import patterns, url

from team import views

urlpatterns = patterns('',
    url(r'^$', views.teams, name='teams'),
    url(r'^(\d+)/$', views.teams_team, name='teams'),
    
)