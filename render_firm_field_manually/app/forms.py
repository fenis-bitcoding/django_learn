from django import forms

class UserRegi(forms.Form):
    name = forms.CharField(help_text="Please enter the name")
    email = forms.EmailField()