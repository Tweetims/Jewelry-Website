# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views as home_views
from apps.calendar_app import views as calendar_views

urlpatterns = [
    path('', home_views.index, name='home'),
    
    path('courses', calendar_views.course_calendar, name='courses'),
    path('courses/<int:year>/<str:month>/', calendar_views.course_calendar, name='course_calendar'),
    path('courses/<int:year>/<str:month>', calendar_views.course_calendar, name='course_calendar'),
    
    path('courses/all', home_views.course_list, name='course_list'),
    path('courses/view/<course_id>/', home_views.course_view, name='course_view'),
    path('courses/add', home_views.add_course, name='add_course'),
    path('courses/edit', home_views.edit_course, name='edit_course'),
    path('courses/edit/<course_id>/', home_views.edit_course_id, name='edit_course_id'),
    path('courses/delete/<course_id>/', home_views.delete_course_id, name='delete_course_id'),
    path('courses/signup/<course_id>/', home_views.course_sign_up, name='course_sign_up'),

    path('account', home_views.user_page, name='user_page'),
    path('settings', home_views.user_settings, name='user_settings'),
    
    path('how-it-works', home_views.info_templates, name='how_it_works'),
    path('about', home_views.home_templates, name='about'),
    path('contact', home_views.home_templates, name='contact'),

    # Matches any html file within the templates dir
    # also requires a login
    #re_path(r'^.*\.*', home_views.template_templates, name='pages'),

]
