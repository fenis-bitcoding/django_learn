from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user nu account delete kariye to tyare teni post ma null avi jase 
    # user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()


class song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=255)
    song_duration = models.IntegerField()

    def written_by(self):
        return ','.join([str(p) for p in self.user.all()])