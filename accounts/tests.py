from django.test import TestCase

# Create your tests here.
class TestURLS(TestCase):
    def testUsers(self):
        self.assertEquals(self.client.get('/account/register/').status_code, 200)
        self.assertEquals(self.client.get('/account/login/').status_code, 200)