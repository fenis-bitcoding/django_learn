from django.shortcuts import render
from .models import user
# Create your views here.
def query(request):
    hh = user.objects.all()
    for i in hh:
        print(i.name,i.age)    
    return render(request , 'check.html',{'hh':hh})    