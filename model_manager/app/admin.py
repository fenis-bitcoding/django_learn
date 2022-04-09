from django.contrib import admin
from .models import Student,User,Employe,ProxyStudent
# Register your models here.
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']

@admin.register(Employe)
class EmployeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']

@admin.register(ProxyStudent)
class ProxyStudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']