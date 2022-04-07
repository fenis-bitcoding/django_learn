from django.db import models


# Create your models here.
class user(models.Model):
    user = models.CharField(max_length=25)
    roll = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()


    def __str__(self):
        return self.user

class techer(models.Model):
    user= models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
