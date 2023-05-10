from django.test import TestCase


# home page test
class HomepageTest(TestCase):
    def setup(self):
        return

    def test_Homepage(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)


# create poi API test
class CreatePoiTest(TestCase):
    def setup(self):
        return

    def test_animals(self):
        response = self.client.post('/api/poi', {'name': 'test name', 'animal_name': 'fox', 'latitude': '1', 'longitude': '1', 'image': 'https://www.woodlandtrust.org.uk/media/1394/fox-flickr-adrian-coleman.jpg'})

        self.assertEquals(response.status_code, 200)


# view poi test
class ViewPoiTest(TestCase):
    def setup(self):
        return

    def test_animals(self):
        response = self.client.get('/api/pois')

        self.assertEquals(response.status_code, 200)
