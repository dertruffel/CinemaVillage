# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.IntegerField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title + ', ' + str(self.author)
