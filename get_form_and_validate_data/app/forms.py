from django import forms
from django.core import validators
class UserRegi(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(4)])
    email = forms.EmailField()
    password = forms.CharField()
    retype_password = forms.CharField()

    def clean(self) :
        cleaned_data = super().clean()
        val_password = self.cleaned_data['password']
        valrpassword = self.cleaned_data['retype_password']
        if val_password != valrpassword :
            raise forms.ValidationError('password does not match')