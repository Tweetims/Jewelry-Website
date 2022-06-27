# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    path('courses', views.events, name='events'),
    path('courses/<int:year>/<str:month>/', views.events, name='events'),
    
    path('courses/all', views.event_list, name='event_list'),
    path('courses/add', views.add_event, name='add_event'),
    
    
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
