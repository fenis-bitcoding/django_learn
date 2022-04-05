from django.shortcuts import render
from .forms import UserRegi
# Create your views here.
def home(request):
    form = UserRegi()
    return render(request,'first.html',{'form':form})