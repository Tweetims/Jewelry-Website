# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.home import views as home_views

urlpatterns = [
    path('', home_views.index, name='home'),
    


    path('account', home_views.user_page, name='user_page'),
    path('settings', home_views.user_settings, name='user_settings'),

    path('designs', home_views.design_search, name='designs'),
    path('designs/<uuid>', home_views.course_sign_up, name='course_sign_up'),
    
    path('how-it-works', home_views.info_templates, name='how_it_works'),
    path('about', home_views.home_templates, name='about'),
    path('contact', home_views.home_templates, name='contact'),

    # Matches any html file within the templates dir
    # also requires a login
    #re_path(r'^.*\.*', home_views.template_templates, name='pages'),

]
