# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import WebsiteUser
from .models import Event

admin.site.register(WebsiteUser)
admin.site.register(Event)
