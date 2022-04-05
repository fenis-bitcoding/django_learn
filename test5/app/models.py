from queue import Empty
from re import T
from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=24)
    surname = models.CharField(max_length=23)
    age = models.IntegerField()
    email = models.EmailField()
    DOB = models.DateField(blank=True)
    test = models.CharField(max_length=255,blank=True)
