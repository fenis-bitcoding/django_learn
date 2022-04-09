from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    roll_No = models.IntegerField()
  


