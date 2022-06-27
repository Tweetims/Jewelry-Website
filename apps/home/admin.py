# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import WebsiteUser
from .models import Event

#admin.site.register(WebsiteUser)
#admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'event_date')
    ordering = ('-event_date',)
    search_fields = ('name', 'event_date', 'description')
    list_filter = ('name', 'event_date')
    

@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ('first_name',  'last_name', 'email', 'phone')
    ordering = ('last_name',)
    search_fields = ('first_name', 'last_name', 'email', 'phone')