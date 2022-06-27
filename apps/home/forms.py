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
        ))
    event_date = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": datetime.date(datetime.now()),
                "class": "form-control",
                'value': datetime.date(datetime.now())
            }
        ))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Event Description",
                "class": "form-control"
            }
        ))
    course_fee = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Event Fee",
                "class": "form-control",
                'value': 200,
                'min': 0
            }
        ))
    maximum_capacity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "10",
                "class": "form-control",
                'value': 10,
                'min': 1,
                'max': 15
            }
        ))
    
    class Meta:
        model = Event
        fileds = ('name', 'event_date', 'description', 'course_fee',)
        exclude = ('attendees',)