from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='index')
)