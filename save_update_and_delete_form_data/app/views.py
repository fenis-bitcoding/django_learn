from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegi
from .models import User
# Create your views here.

def home(request):
    if request.method == "POST":
        form = UserRegi(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            regi = User(name=name,email=email,password=password)
            regi.save()
            return HttpResponseRedirect('/')
    else:
        form = UserRegi()
    return render(request, 'home.html',{'form':form})        
