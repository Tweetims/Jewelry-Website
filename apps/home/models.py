# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from enum import auto
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    email = models.EmailField('User Email', max_length=256, null=True)
    phone = models.CharField('User Phone Number', max_length=20, blank=True, null=True)
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return f'{self.email}'


class Tag(models.Model):
    name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField('Design Image')
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.image)


class Design(models.Model):
    name = models.CharField('Design Name', max_length=256)
    description = models.TextField('Description', max_length=2048, null=True)
    notes = models.TextField('Notes', max_length=2048, blank=True, null=True)
    images = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.name)


class Course(models.Model):
    name = models.CharField('Course Name', max_length=256)
    course_date = models.DateField('Course Date')
    start_time = models.TimeField('Start Time', default='12:00')
    end_time = models.TimeField('End Time', default='13:00')
    description = models.TextField('Course Description', max_length=2048)
    attendees = models.ManyToManyField(WebsiteUser, blank=True)
    course_fee = models.PositiveIntegerField('Course Fee', blank=True, default=200)
    maximum_capacity = models.PositiveIntegerField('Maximum Capacity', blank=True, default=10)
    designs = models.ManyToManyField(Design)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.name)
