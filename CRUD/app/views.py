from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegi
from .models import User
# Create your views here.

def index(request):
    if request.method == "POST" :
        form = UserRegi(request.POST,label_suffix=" ")
        if form.is_valid():
            username = form.cleaned_data['username']
            email  = form.cleaned_data['email']
            password = form.cleaned_data['password']
            roll_no = form.cleaned_data['roll_No']
            regi = User(username=username,email=email,password=password,roll_No=roll_no)
            regi.save()
            return HttpResponseRedirect('/')
    else:
        form = UserRegi(label_suffix=" ")
    stud = User.objects.all()
    return render(request,'index.html',{'form':form,"stud" : stud })

def Edit(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        form = UserRegi(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        form = UserRegi(instance=pi)
    return render(request,'edit.html',{'form':form})

def delete(request,id):
    if request.method == 'POST':
        pi  = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

    