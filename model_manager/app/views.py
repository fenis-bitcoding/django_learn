from django.shortcuts import render
from .models import Employe, Student,User,ProxyStudent
# Create your views here.
def home(request):
    # form = Student.objects.all()
    form = Student.Students.all()
    return render(request,"home.html",{'form':form})

def index(request):
    # form = User.objects.all()
    form = User.Students_User.all()
    return render(request,'index.html',{'form':form})

def data(request):
    # form = Employe.objects.all()
    form = Employe.Students_Roll_User.get_stu_roll_range(1,9)
    return render(request,'employe.html',{'form':form})

def info(request):
    form = ProxyStudent.students_proxy.get_stu_roll_range(101,111)
    return render(request,'pstu.html',{'form':form})