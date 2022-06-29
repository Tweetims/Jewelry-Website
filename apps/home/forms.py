from django import forms
from django.forms import ModelForm
from .models import Event

from datetime import datetime

class EventForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Event Name",
                "class": "form-control"
            }
        ),
        label='Name')
    event_date = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Date",
                "class": "form-control",
                'value': datetime.date(datetime.now())
            }
        ),
        label='Date')
    event_time = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": 'Time',
                "class": "form-control",
                'value': "12:00"
            }
        ),
        label='Time')
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
        model = Event
        fileds = ('name', 'event_date', 'event_time', 'description', 'course_fee',)
        exclude = ('attendees',)