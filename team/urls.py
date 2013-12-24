from django.conf.urls import patterns, url

from team import views

urlpatterns = patterns('',
    url(r'^$', views.standings, name='standings'),
    url(r'^standings/(\d+)/$', views.standings_team, name='standings_team'),
    url(r'^teams/', views.teams, name='teams'),
    
)