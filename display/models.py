# Create your models here.
from django.utils import timezone
today = timezone.now

from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    id = models.BigAutoField(primary_key= True, auto_created= True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None, blank = True)
    description = models.CharField(max_length=255,default=None, blank = True)
    cost = models.IntegerField()
    image = models.ImageField(upload_to='',default=None, blank = True)
    like = models.ManyToManyField(User, related_name="like",default=None, blank = True)
    date = models.DateField(default=today,blank = True)
    location = models.CharField(max_length=255,default=None, blank = True)

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.like.count()

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return str(self.event)
    def ticket_id(self):
        return self.id
    def ticket_owner(self):
        return self.owner
