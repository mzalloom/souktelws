#!usr/bin/env python
# encoding=utf-8
# Mohannad Zalloom

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url(r'^survey/?$', views.index),
    url(r'^survey/(\d+)/?$', views.profile, name='profile')
)