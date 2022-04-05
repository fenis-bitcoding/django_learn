import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegi
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserRegi(request.POST)
        if form.is_valid():
            # print(form)
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            return HttpResponseRedirect('/')
    else:
        form = UserRegi()
        print("ggggg")
    return render(request, 'forms.html',{'form':form})