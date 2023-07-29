from django import forms
from django.forms import ModelForm
from .models import WebsiteUser, CourseSignUp, METAL_TYPES, KARAT


class CourseSignUpForm(ModelForm):
    metal_type = forms.ChoiceField(
        choices=METAL_TYPES,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        label="Select Metal Types",
        required=True
    )

    purity = forms.ChoiceField(
        choices=KARAT,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        label="Select Purity",
        required=True
    )

    date1 = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Course Date"
    )

    date2 = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Second Course Date"
    )

    class Meta:
        model = CourseSignUp
        fields = ('metal_type', 'purity', 'date1')

    def clean(self):
        super(CourseSignUpForm, self).clean()

        metal_type = self.cleaned_data.get('metal_type')
        purity = self.cleaned_data.get('purity')

        if metal_type == 'SV' and purity != '925s':
            self._errors['metal_type'] = self.error_class([
                'Sterling Silver must be selected with Silver.'
            ])

        return self.cleaned_data


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
