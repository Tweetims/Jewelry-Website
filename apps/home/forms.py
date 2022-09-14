from django import forms
from django.forms import ModelForm
from .models import Course
from datetime import datetime


class CourseForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Course Name",
                "class": "form-control"
            }
        ),
        label='Name')
    course_date = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Date",
                "class": "form-control",
                'value': datetime.date(datetime.now())
            }
        ),
        label='Date')
    start_time = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": 'Time',
                "class": "form-control",
                'value': "12:00 PM"
            }
        ),
        label='Start Time')
    end_time = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": 'Time',
                "class": "form-control",
                'value': "02:00 PM"
            }
        ),
        label='End Time')
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Event Description",
                "class": "form-control",
                "rows": "4"
            }
        ),
        label='Description')
    course_fee = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Event Fee",
                "class": "form-control",
                'value': 200,
                'min': 0
            }
        ),
        label='Fee')
    maximum_capacity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "10",
                "class": "form-control",
                'value': 10,
                'min': 1,
                'max': 15
            }
        ),
        label='Seats')
    
    class Meta:
        model = Course
        fileds = ('name', 'course_date', 'course_time', 'description', 'course_fee',)
        exclude = ('attendees',)