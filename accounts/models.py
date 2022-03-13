from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=32,null=True)
    password=models.CharField(max_length=32,null=True)
    email=models.CharField(max_length=32,null=True)

    def __str__(self):
        return self.username