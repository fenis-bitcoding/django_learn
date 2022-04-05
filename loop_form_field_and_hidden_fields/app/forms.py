from django import forms

class UserRegi(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    retype = forms.CharField(widget=forms.HiddenInput())
