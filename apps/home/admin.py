# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import WebsiteUser, Course, Design, Image, Tag, WaxConversion, CourseSignUp, User


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course_date',)
    ordering = ('-course_date',)
    search_fields = ('name', 'course_date', 'description', 'tags',)
    list_filter = ('name', 'course_date', 'tags',)


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(WaxConversion)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(CourseSignUp)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('course', 'account',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    

@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('first_name',  'last_name', 'email', 'phone',)
    ordering = ('last_name',)
    search_fields = ('first_name', 'last_name', 'email', 'phone',)
