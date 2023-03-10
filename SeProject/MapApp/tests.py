from django.test import TestCase

# Create your tests here.

class HomepageTest(TestCase):
    def setup(self):
        return

    def test_Homepage(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)
        
class AnimalsTest(TestCase):
    def setup(self):
        return

    def test_animals(self):
        response = self.client.get('/api/animals')

        self.assertEquals(response.status_code, 200)