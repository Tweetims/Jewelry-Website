# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views as home_views
from apps.calendar_app import views as calendar_views

urlpatterns = [

    # The home page
    path('', home_views.index, name='home'),
    
    path('courses', calendar_views.event_calendar, name='events'),
    #path('courses/<int:year>/<str:month>/', home_views.events, name='events'),
    
    path('courses/all', home_views.event_list, name='event_list'),
    path('courses/add', home_views.add_event, name='add_event'),
    path('courses/edit', home_views.edit_event, name='edit_event'),
    path('courses/edit/<event_id>/', home_views.edit_event_id, name='edit_event_id'),
    path('courses/delete/<event_id>/', home_views.delete_event_id, name='delete_event_id'),
    
    
    path('about', home_views.about, name='about'),
    path('contact', home_views.contact, name='contact'),

    # Matches any html file
    re_path(r'^.*\.*', home_views.pages, name='pages'),

]
