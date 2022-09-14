# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import WebsiteUser
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course_date')
    ordering = ('-course_date',)
    search_fields = ('name', 'course_date', 'description')
    list_filter = ('name', 'course_date')
    

@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('first_name',  'last_name', 'email', 'phone')
    ordering = ('last_name',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')