from django.db import models
from .managers import CustomManager,CustomRangeManager
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll  = models.IntegerField()
    Students = models.Manager()

class User(models.Model):
    name = models.CharField(max_length=70)
    roll  = models.IntegerField()
    objects = models.Manager()
    Students_User = CustomManager()

class Employe(models.Model):
    name = models.CharField(max_length=70)
    roll  = models.IntegerField()
    objects =  models.Manager()
    Students_Roll_User = CustomRangeManager()

class ProxyStudent(Student):
    students_proxy = CustomRangeManager()
    proxy = True
    ordering = ['name']