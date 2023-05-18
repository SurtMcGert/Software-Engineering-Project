from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse, reverse_lazy

from .models import Badge, User, UserProfile


# Create your tests here.
class DisplayProfileTestCase(TestCase):
    def setUp(self):
        # Create a test user and profile
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user)

    # I have no idea why this 404s
    def test_display_profile_authenticated(self):
        # Create a client and log in the user
        client = Client()
        client.login(username='testuser', password='testpassword')

        print("Users: ", get_object_or_404(UserProfile, user=self.user))

        # Prepare the URL for the GET request
        url = reverse('displayProfile')

        # Make the GET request
        response = client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the context data
        self.assertEqual(response.context['name'], 'testuser')
        self.assertListEqual(list(response.context['badges']), list(self.profile.badges.all()))

        # Assert the rendered template
        self.assertTemplateUsed(response, 'ProfileApp/userProfile.html')

class CreateProfileTestCase(TestCase):
    def test_create_profile(self):
        # Create a test user
        user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a test badge
        badge = Badge.objects.create(name='welcome')
        
        # Prepare the URL for the GET request
        url = reverse('createProfile', args=[user.id])
        
        # Make the GET request
        response = self.client.get(url)
        
        # Assert the response status code
        self.assertEqual(response.status_code, 302)  # Redirect
        
        # Refresh the user profile from the database
        user_profile = UserProfile.objects.filter(user=user).first()
        
        # Assert the user profile exists and has the badge
        self.assertIsNotNone(user_profile)
        self.assertIn(badge, user_profile.badges.all())