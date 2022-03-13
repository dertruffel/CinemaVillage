from django.contrib import admin
# Register your models here.
from .models import Event


"""
EVENT
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.IntegerField()
    image = models.ImageField()
"""
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','author','description','cost','image']
