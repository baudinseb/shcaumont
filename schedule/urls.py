from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('',
    url(r'^$', views.regular, name='regular'),
    url(r'^regular/(\d+)/$', views.regular_team, name='regular_team'),
    url(r'^cup/$', views.cup, name='cup'),
    url(r'^cup/(\d+)/$', views.cup_team, name='cup_team'),
    url(r'^playoffs/$', views.playoffs, name='playoffs'),
    url(r'^playoffs/(\d+)/$', views.playoffs_team, name='playoffs_team'),
)