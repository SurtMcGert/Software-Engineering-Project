from django.core import mail
from django.test import TestCase
from django.urls import reverse

from .models import Poi


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

class ApiPoisTestCase(TestCase):
    def test_api_pois(self):
        # Create some test POIs
        poi1 = Poi.objects.create(name='POI 1', latitude=12.345, longitude=67.890, image='https://www.woodlandtrust.org.uk/media/1394/fox-flickr-adrian-coleman.jpg')
        poi2 = Poi.objects.create(name='POI 2', latitude=98.765, longitude=43.210)

        # Prepare the URL for the GET request
        url = reverse('api_pois')

        # Make the GET request
        response = self.client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_data = [
            {
                'id': poi1.id,
                'name': 'POI 1',
                'latitude': 12.345,
                'longitude': 67.890
            },
            {
                'id': poi2.id,
                'name': 'POI 2',
                'latitude': 98.765,
                'longitude': 43.210
            }
        ]
        self.assertEqual(response.json(), expected_data)       


class PrivacyTestCase(TestCase):
    def test_privacy_view(self):
        # Prepare the URL for the view
        url = reverse('privacy')

        # Make the GET request
        response = self.client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response template used
        self.assertTemplateUsed(response, 'privacy.html')

class AssertationsTestCase(TestCase):
    def test_privacy_view(self):
        # Prepare the URL for the view
        url = reverse('assertations')

        # Make the GET request
        response = self.client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response template used
        self.assertTemplateUsed(response, 'assertations.html')

class ContactTestCase(TestCase):
    def test_contact_view(self):
        # Prepare the URL for the view
        url = reverse('contact')

        # Make a POST request with valid form data
        response = self.client.post(url, {
            'name': 'John Doe',
            'subject': 'Test Subject',
            'email': 'johndoe@example.com',
            'message': 'Test message',
        })

        # Assert the response status code and redirection
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('map'))

        # Assert that an email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Assert the email contents
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, 'Test Subject')
        self.assertEqual(sent_email.body, 'John Doe:\nTest message')
        self.assertEqual(sent_email.from_email, 'johndoe@example.com')
        self.assertEqual(sent_email.to, ['wildWorld@gmail.com'])

    def test_contact_view_invalid_form(self):
        # Prepare the URL for the view
        url = reverse('contact')

        # Make a POST request with invalid form data
        response = self.client.post(url, {
            'name': 'John Doe',
            'subject': '',
            'email': 'johndoe@example.com',
            'message': 'Test message',
        })

        # Assert the response status code and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)