from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_DEFAULT
import datetime 
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    organizer = models.ForeignKey(User,on_delete=CASCADE)
    event_title = models.CharField(max_length=30,default='Event Title')
    event_subtitle = models.CharField(max_length=100,blank=True)
    location = models.CharField(max_length=50,blank=True)
    date = models.DateTimeField(blank=True)
    time = models.TimeField(default=datetime.time(10, 00, 00))
    description = models.TextField(blank=True)
    category = models.CharField(max_length=25,default="Other")


    def __str__(self):
        return self.event_title


class Profile(models.Model):
    name = models.ForeignKey(User,on_delete=CASCADE)
    age = models.IntegerField(default=18)
    gender = models.CharField(default="MALE",max_length=15)
    location = models.CharField(default="Coimbatore",max_length=25)
    role = models.CharField(default="participant",max_length=20)

class Tags(models.Model):
    tag_per_post = models.CharField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=CASCADE)
    content = models.TextField()
    img = models.ImageField(upload_to='posts')
    time = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tags,blank=True)
    likes = models.IntegerField(default=0,blank=True)
    comments = models.IntegerField(default=0,blank=True)



class Particpations(models.Model):
    participant = models.ForeignKey(User,on_delete=CASCADE)
    events = models.ForeignKey(Event,on_delete=CASCADE)
