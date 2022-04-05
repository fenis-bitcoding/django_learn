from django import forms

class UserRegi(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()