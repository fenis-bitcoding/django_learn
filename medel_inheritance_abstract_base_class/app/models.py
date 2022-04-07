from django.db import models

# Create your models here.
class Commoninfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True
        
class Student(Commoninfo):
    fees = models.IntegerField()
    date = None
    def __str__(self):
        return self.name
           
           
class Teacher(Commoninfo):
    salary = models.IntegerField()
    def __str__(self):
        return self.name
    
class Contractor(Commoninfo):
    payment = models.IntegerField()
    date = models.DateTimeField() 
    def __str__(self):
        return self.name 
