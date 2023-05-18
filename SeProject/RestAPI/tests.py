from decimal import Decimal, getcontext

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from DiscussionApp.models import DiscussionBoard
from MapApp.models import Poi
from ProfileApp.models import UserProfile

from .serializers import (DiscussionBoardSerializer, PoiSerializer,
                          UserSerializer)


# Create your tests here.
class PoiViewSetTest(TestCase):
    # This should work, but due to problems with the decimal format it fails
    def test_serialize_poi(self):
        getcontext().prec=7
        
        poi = Poi.objects.create(name='Test POI', latitude=123.456, longitude=789.012,
                                 animal_name='Test Animal', scientific_name='Test Scientific',
                                 locations='Test Location', feature='Test Feature',
                                 slogan='Test Slogan', habitat='Test Habitat')
        serializer = PoiSerializer(poi)
        expected_data = {
            'id': poi.id,
            'name': 'Test POI',
            'latitude':Decimal(123.456),
            'longitude':Decimal(789.012),
            'animal_name': 'Test Animal',
            'scientific_name': 'Test Scientific',
            'locations': 'Test Location',
            'feature': 'Test Feature',
            'slogan': 'Test Slogan',
            'habitat': 'Test Habitat'
        }

        self.assertEqual(serializer.data, expected_data)
    
    def test_PoiViewSet(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

class UserViewSetTest(TestCase):
    def setup(self):
        return

    def test_serialize_user(self):
        user = User.objects.create(username='testuser')
        serializer = UserSerializer(user)
        expected_data = {'id': user.id, 'username': 'testuser'}

        self.assertEqual(serializer.data, expected_data)

    def test_UserViewSet(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

class DiscussionBoardViewSetTest(TestCase):
    def setUp(self):
        self.poi = Poi.objects.create(
            name="Test POI",
            latitude=Decimal("40.7128"),
            longitude=Decimal("-74.0060"),
            animal_name="Test Animal",
            scientific_name="Test Scientific Name",
            locations="Test Location",
            feature="Test Feature",
            slogan="Test Slogan",
            habitat="Test Habitat"
        )
        self.discussion = DiscussionBoard.objects.create(poi=self.poi)

    def test_discussion_board_serializer(self):
        serializer = DiscussionBoardSerializer(instance=self.discussion)
        expected_data = {
            "id": self.discussion.id,
            "poi": 1
        }
        self.assertEqual(serializer.data, expected_data)

    def test_DiscussionBoardViewSet(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

class ChatMessageViewSetTest(TestCase):
    def setup(self):
        return

    def test_ChatMessageViewSet(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

class BadgeViewSetTest(TestCase):
    def setup(self):
        return

    def test_BadgeViewSet(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)

class UserProfileViewSetTest(TestCase):
    def setup(self):
        self.client = APIClient()

    def test_UserProfileViewSet(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)
