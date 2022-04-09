from cProfile import label
from django import forms
from .models import User

class UserRegi(forms.ModelForm):
    class Meta :
        model = User
        fields = ['username' , 'email' , 'password' , 'roll_No']
        error_messages = {
            'username':{'required':"Enter Username"},
            'email' : {'required' : 'Enter Email'},
            'password':{'required':"Enter Password"},
            'roll_No' : {'required' : "Enter Roll No."}
            }

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'Enter Password'}),
            'roll_No' : forms.NumberInput(attrs={'class' : 'form-control','placeholder':'Enter Roll No.'})
        }
        