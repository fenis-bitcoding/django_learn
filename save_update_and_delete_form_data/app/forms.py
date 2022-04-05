from django import forms
from django.core import validators

class UserRegi(forms.Form):
    name = forms.CharField(error_messages={'required':'enteryour name'})
    email = forms.EmailField(error_messages={'required':'enteryour email'})
    password = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'enteryour Password'})