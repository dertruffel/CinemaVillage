from django.test import TestCase


# Create your tests here.

class TestURLS(TestCase):
    def testIndex(self):
        self.assertEquals(self.client.get('/').status_code, 200)

    def testBuying(self):
        self.assertEquals(self.client.get('/buy').status_code, 200)

    def testHistory(self):
        self.assertEquals(self.client.get('/history').status_code, 200)
