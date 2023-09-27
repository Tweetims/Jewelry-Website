# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from django.utils.html import mark_safe
from django.utils.timezone import now
from apps.home.storage_backends import PublicMediaStorage


class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    email = models.EmailField('User Email', max_length=256, null=True)
    phone = models.CharField('User Phone Number', max_length=20, blank=True, null=True)
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True, editable=True)
    
    def __str__(self) -> str:
        return f'{self.account}'

    def name(self):
        return f'{self.last_name}, {self.first_name}'


class Tag(models.Model):
    name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField('Image Name', max_length=256, default='FILE_NAME')
    image = models.ImageField('Design Image', blank=True, default='no_image.jpg', null=True, storage=PublicMediaStorage())

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.name == "FILE_NAME":
            self.name = self.image.name.split('.')[:-1][0]
        super(Image, self).save(*args, **kwargs)

    def get_image(self):
        try:
            return self.image.url
        except:
            return 'https://jcs-bucket.sfo3.digitaloceanspaces.com/jcs-bucket/media/no_image.jpg'

    def image_preview(self):
        return mark_safe(f'<img src="{self.get_image()}" width="300"/>')

    def image_preview_200w(self):
        return mark_safe(f'<img src="{self.get_image()}" width="300" class="max-width-200 pb-1"/>')

    def image_preview_card(self):
        return mark_safe(f'<img src="{self.get_image()}" class="card w-100"/>')


class Design(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField('Design Name', max_length=256)
    description = models.TextField('Description', max_length=2048, null=True)
    notes = models.TextField('Notes', max_length=2048, blank=True, null=True)
    images = models.ManyToManyField(Image)
    tags = models.ManyToManyField(Tag)
    weight = models.FloatField('Metal Weight', default=0)
    ctw = models.FloatField('Total Carat Weight', default=0)
    course_fee = models.PositiveIntegerField('Course Fee', blank=True, default=200)

    def __str__(self) -> str:
        return f'{self.name}'

    def get_image(self):
        try:
            image = self.images.all()[0].image
        except:
            image = 'no_image.jpg'
        return mark_safe(f'{self.name}<img src="{PublicMediaStorage().get_full_url()}/{image}" width="300"/>')


KARAT = (
    ('10k', '10K Gold'),
    ('14k', '14K Gold'),
    ('18k', '18K Gold'),
    ('925s', 'Sterling Silver'),
)

METAL_TYPES = (
    ('YG', 'Yellow Gold'),
    ('WG', 'White Gold'),
    ('RG', 'Rose Gold'),
    ('SV', 'Silver'),
)


def datetime_now():
    return now()


class CourseSignUp(models.Model):
    account = models.ForeignKey(to=WebsiteUser, on_delete=models.CASCADE, editable=True)
    date1 = models.DateField('First Course Date', default=datetime_now, null=True)
    date2 = models.DateField('Second Course Date', default=datetime_now, null=True)
    design = models.ForeignKey(to=Design, on_delete=models.CASCADE)
    metal_type = models.CharField('Metal Type', choices=METAL_TYPES, max_length=128)
    purity = models.CharField('Purity', choices=KARAT, max_length=128)
    checked_in = models.BooleanField('Checked In', default=False)

    def __str__(self):
        return f'{self.account.name()} {self.design} {self.purity} {self.metal_type}'

    def design_preview(self):
        try:
            image = self.design.images.all()[0].image
        except:
            image = 'no_image.jpg'
        return mark_safe(f'{self.name}<img src="{PublicMediaStorage().get_full_url()}/{image}" width="300"/>')
