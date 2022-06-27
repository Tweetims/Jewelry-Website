# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.videos import views

urlpatterns = [
    
    path('videos', views.index, name='videos'),

]
