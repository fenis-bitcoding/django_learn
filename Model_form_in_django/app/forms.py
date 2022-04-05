from django import forms
from .models import User

class UserRegi(forms.ModelForm):
    name = forms.CharField(max_length=50,required=True)
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
        error_messages = {
            'name' : {'required' : 'Please Enter The Name'},
            'email' : {'required' : 'Please Enter The Email'},
            'password' : {'required' : 'Please Enter The Password'},
        }
        widgets = {
            'password' : forms.PasswordInput,
            'name': forms.TextInput(attrs={'class': 'myclass','placeholder' : 'Enter Name'}),
            
        }
