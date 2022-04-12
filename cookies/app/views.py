from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def setcookie(request):
    reponse =  render(request,'student/setcookie.html')
    reponse.set_cookie('name','fenis',expires=datetime.utcnow()+timedelta(day=2))
    return reponse

def getcookie(request):
    name = request.COOKIES.get('name')
    return render(request,'student/getcookie.html',{'cook':name})

def delcookie(request):
    respose = render(request, 'student/delcookie.html')
    respose.delete_cookie('name')
    return respose

