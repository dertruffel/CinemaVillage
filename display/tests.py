from django.http import HttpRequest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import *
from .views import *
from accounts import tests

# Create your tests here.


""" id = models.BigAutoField(primary_key= True, auto_created= True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.IntegerField()
    image = models.ImageField(upload_to='')
    like = models.ManyToManyField(User, related_name="like",default=None, blank = True)
    date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=255, default=None)"""


class TestURLS(TestCase):

    def testIndex(self):
        self.assertEquals(self.client.get('/').status_code, 200)

    def setUp(Event) -> None:
        Event.id = 1
        Event.title = 'test_title'
        Event.author = 'admin'
        Event.description = 'desc'
        Event.cost = 20


    def testBuying(self):

        self.setUp()
        get_user_model().objects.create(username="username", password="password")
        self.client.login(username="username",password="password")
        request = HttpRequest()
        response = self.client.post(buyTicket(request=self.client,pk=Event.id))
        self.assertEqual(response.status_code, 302) #redirect after purchase

    def testHistory(self):
        self.assertEquals(self.client.get('/tickets/').status_code, 200)
