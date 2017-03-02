#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from geonode.contrib.risks import views

extraction_urls = [
    url(r'^$', views.risk_data_extraction_index, name='data_extraction_index'),
    url(r'loc/(?P<loc>[\w\-]+)/ht/(?P<ht>[\w\-]+)/at/(?P<at>[\w\-]+)/$', views.risk_data_extraction_index, name='data_extraction'),
    url(r'loc/(?P<loc>[\w\-]+)/ht/(?P<ht>[\w\-]+)/at/(?P<at>[\w\-]+)/dym/(?P<dym>[\w\-]+)/$', views.risk_data_extraction_index, name='data_extraction_dym'),
    url(r'loc/(?P<loc>[\w\-]+)/ht/(?P<ht>[\w\-]+)/at/(?P<at>[\w\-]+)/dym/(?P<dym>[\w\-]+)/an/(?P<an>[\w\-]+)/$', views.risk_data_extraction_index, name='data_extraction_analysis'),
]

urlpatterns = [
    url(r'^cost_benefit/$', views.cost_benefit_index, name='risks_cost_benefit_index'),
    url(r'^risk_data_extraction/', include(extraction_urls, namespace='risks')),
]