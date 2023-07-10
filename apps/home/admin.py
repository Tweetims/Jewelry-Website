# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import WebsiteUser, Course, Design, Image, Tag, CourseSignUp, \
    CourseDay


class CourseDayInline(admin.TabularInline):
    model = CourseDay
    extra = 0


class CourseSignUpInline(admin.TabularInline):
    model = CourseSignUp
    readonly_fields = ('account', 'design', 'design_preview', 'metal_type')
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'dates',)
    search_fields = ('name', 'description', 'tags',)
    list_filter = ('name', 'tags',)
    inlines = [CourseDayInline, CourseSignUpInline, ]
    readonly_fields = ['designs_preview']

    @staticmethod
    def dates(request):
        return list(request.courseday_set.all())


@admin.register(CourseDay)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('date', 'start', 'end', 'course')
    search_fields = ('date', 'course',)
    list_filter = ('date', 'course',)

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(CourseSignUp)
class DesignAdmin(admin.ModelAdmin):
    ordering = ('course', 'account',)

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    readonly_fields = ['image_preview']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('name',)
    

@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'account', 'first_name',  'last_name', 'phone',)
    ordering = ('last_name',)
    search_fields = ('first_name', 'last_name', 'email', 'phone',)
