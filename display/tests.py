
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib import auth

from django.urls import reverse

import accounts.tests
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

    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password123!'

    def testBuying(self):
        user = get_user_model().objects.create(username=self.username, password=self.password)
        response = self.client.post(reverse('login'), data={
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.is_authenticated,True)
        requester=self
        requester.user=user
        test_makeEvent(user)
        response = buyTicket(requester,pk=Event.pk,test=1)
        self.assertEqual(response.status_code, 302)  # redirect after purchase
        ticket = get_object_or_404(Ticket, id=1)
        self.assertEqual(user.id,ticket.owner_id)

    def testHistory(self):
        self.assertEquals(self.client.get('/tickets/').status_code, 200)
