from django.contrib import admin
# Register your models here.
from .models import Event,Ticket

"""
EVENT
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.IntegerField()
    image = models.ImageField()
"""
admin.site.register(Event)
admin.site.register(Ticket)

"""
 Ticket(models.Model):
    title = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_title")
    cost = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_cost")
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_username")
    """
