# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import WebsiteUser, Design, Image, Tag, CourseSignUp


class CourseSignUpInline(admin.TabularInline):
    model = CourseSignUp
    readonly_fields = ('design', 'design_preview', 'metal_type')
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(CourseSignUp)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('account',)

    def has_add_permission(self, request, obj=None):
        return True


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    readonly_fields = ['image_preview', 'url']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    

@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'account', 'first_name',  'last_name', 'phone',)
    ordering = ('last_name',)
    search_fields = ('first_name', 'last_name', 'email', 'phone',)
