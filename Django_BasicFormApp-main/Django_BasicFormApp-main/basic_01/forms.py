from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z")

class FormName(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, validators=[check_for_z])
    email = forms.EmailField(label='Your email', max_length=100)
    verify_email = forms.EmailField(label='Verify email', max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vemail = cleaned_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure emails match!")