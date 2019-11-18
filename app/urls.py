#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^getinfo', views.getInfo, name='getinfo'),
    url(r'^gethost', views.getHost, name='gethost'),
    url(r'^posthost', views.postHost, name='posthost'),
]