from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Course, WebsiteUser, Design, CourseSignUp
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
        fileds = ('name', 'course_time', 'description', 'course_fee',)
        exclude = ('attendees',)


class CourseSignUpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['design'] = forms.ModelChoiceField(
            queryset=self.instance.course.designs.all(),
            widget=forms.RadioSelect()
        )

    class Meta:
        model = CourseSignUp
        fields = ('design', 'metal_type',)


class WebsiteUserForm(ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ),
        label='First Name',
        required=False)

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ),
        label='Last Name',
        required=False)

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ),
        label='Email')

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone Number",
                "class": "form-control"
            }
        ),
        label='Phone Number',
        required=False)

    class Meta:
        model = WebsiteUser
        fields = '__all__'
        exclude = ['account']
