# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
 
class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField('User Email', max_length=256)
    phone = models.CharField('User Phone Number', max_length=20)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Event(models.Model):
    name = models.CharField('Event Name', max_length=256)
    event_date = models.DateTimeField('Event Date')
    description = models.TextField('Event Description', max_length=256)
    attendees = models.ManyToManyField(WebsiteUser, blank=True)
    
    def __str__(self) -> str:
        return self.name