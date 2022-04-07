from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    if request.method == "POST" :
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            messages.success(request,'account create successfuly')
            form.save()
    else:
        form = SignUpForm()
    return render(request,'home.html',{'form':form})


def User_log(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def profile(request):
    return render(request ,'profile.html')