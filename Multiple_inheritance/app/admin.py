from django.contrib import admin
from .models import ExamCenter,Student
# Register your models here.
@admin.register(ExamCenter)
class ExamCenteradmin(admin.ModelAdmin):
    list_display = ['id','cname','city']

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['id','cname','city','name','roll']