# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from enum import auto
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils.html import mark_safe


class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    email = models.EmailField('User Email', max_length=256, null=True)
    phone = models.CharField('User Phone Number', max_length=20, blank=True, null=True)
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True, editable=False)
    
    def __str__(self) -> str:
        return f'{self.account}'


class Tag(models.Model):
    name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField('Image Name', max_length=256, default='Image')
    url = models.URLField('URL', default='')
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.name)

    def image_preview(self):
        return mark_safe(f'<img src="{self.url}" width="300"/>')


class Design(models.Model):
    uuid = models.UUIDField(default=uuid4(), editable=False)
    name = models.CharField('Design Name', max_length=256)
    description = models.TextField('Description', max_length=2048, null=True)
    notes = models.TextField('Notes', max_length=2048, blank=True, null=True)
    images = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)
    weight = models.FloatField('Wax Weight', blank=True, default=0)
    stones = models.PositiveIntegerField('Number of Stones', blank=True, default=0)

    def __str__(self) -> str:
        return str(self.name)


class Course(models.Model):
    name = models.CharField('Course Name', max_length=256)
    description = models.TextField('Course Description', max_length=2048)
    course_fee = models.PositiveIntegerField('Course Fee', blank=True, default=200)
    maximum_capacity = models.PositiveIntegerField('Maximum Capacity', blank=True, default=10)
    designs = models.ManyToManyField(Design)
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.name)

    def designs_preview(self):
        ret = ''
        for design in self.designs.all():
            ret += f'<img src="{design.images.all()[0].url}" width="100"/>'
        return mark_safe(ret)


class CourseDay(models.Model):
    date = models.DateField('Course Date')
    start = models.TimeField('Start Time', default='12:00')
    end = models.TimeField('End Time', default='14:00')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} at {self.start}-{self.end}'


METAL_TYPES = (
    ('silver', 'Silver'),
    ('y10', '10K Yellow Gold'),
    ('y14', '14K Yellow Gold'),
    ('y18', '18K Yellow Gold'),
    ('w10', '10K White Gold'),
    ('w14', '14K White Gold'),
    ('w18', '18K White Gold')
)


class CourseSignUp(models.Model):
    account = models.ForeignKey(to=WebsiteUser, on_delete=models.CASCADE, editable=False)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    design = models.ForeignKey(to=Design, on_delete=models.CASCADE)
    metal_type = models.CharField('Metal Type', max_length=256, choices=METAL_TYPES)

    def __str__(self):
        return f'{self.account} {self.course} {self.design} {self.metal_type}'
