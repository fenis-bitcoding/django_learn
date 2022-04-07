from django.shortcuts import render
from .models import Teacher,Student,Contractor
# Create your views here.
def home(request):
    tech = Teacher.objects.all()
    stu = Student.objects.all()
    con = Contractor.objects.all()
    return render(request,'home.html',{'tech':tech,'stu':stu,'con':con})