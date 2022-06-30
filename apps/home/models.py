# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from enum import auto
from django.db import models
from uuid import uuid4
 
class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField('User Email', max_length=256)
    phone = models.CharField('User Phone Number', max_length=20, blank=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Event(models.Model):
    name = models.CharField('Event Name', max_length=256)
    event_date = models.DateField('Event Date')
    start_time = models.TimeField('Start Time', default='12:00')
    end_time = models.TimeField('End Time', default='13:00')
    description = models.TextField('Event Description', max_length=256)
    attendees = models.ManyToManyField(WebsiteUser, blank=True)
    course_fee = models.PositiveIntegerField('Course Fee', blank=True, default=200)
    maximum_capacity = models.PositiveIntegerField('Maximum Capacity', blank=True, default=10)
    
    def __str__(self) -> str:
        return str(self.name)