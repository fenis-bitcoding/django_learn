from django import forms
class ContractForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()