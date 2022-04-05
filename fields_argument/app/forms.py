from django import forms

class UserRegi(forms.Form):
    # intial value  in name fields
    # important -----> by defualt requerd is True
    # disabled fields means no change in input fields
    # name = forms.CharField(label='First Name',label_suffix=" ",required=False,disabled=True,help_text='Please Fill this fields')
    # email = forms.EmailField()

    name = forms.CharField()
    email = forms.EmailField()