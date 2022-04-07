from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def sign_up(request):
    if request.method == 'POST':

        form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request,'regi.html',{'form':form})