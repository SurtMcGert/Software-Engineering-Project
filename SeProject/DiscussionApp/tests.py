from DiscussionApp.models import ChatMessage, Poi
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ProfileApp.models import UserProfile


# user upvoted check test
class UserUpvotedCheckTest(TestCase):
    
    def setup(self):
        self.client = Client()
        

    def test_user_upvoted_check(self):
        self.user = User.objects.create_user(username='test2', password='1234')
        login = self.client.login(username='test2', password='1234')
        chatMessage = ChatMessage.objects.create(username='test', message="test message", chatroom=1, upvotes=0)
        self.profile = UserProfile.objects.create(user=self.user)
        self.profile.upvotedMessages.set({chatMessage})
        print(login)
        response = self.client.get('/discussion/userUpvotedCheck', {'userID': self.user.id, 'messageID': chatMessage.id})
        print(response.json())
        self.assertEquals(response.json()["success"], True)

class ViewDiscussionTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.poi = Poi.objects.create(name='Test POI', latitude=0.0000001, longitude=0.0000001)
        self.chat_message1 = ChatMessage.objects.create(chatroom=1, message='Message 1')
        self.chat_message2 = ChatMessage.objects.create(chatroom=1, message='Message 2')

    def test_view_discussion(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('loadDiscussionPage', kwargs={'aid': self.poi.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DiscussionApp/discussion.html')
        self.assertEqual(response.context['name'], 'Test POI')
        self.assertEqual(response.context['aid'], str(self.poi.id))
        messages = response.context['messages']
        self.assertEqual(len(messages), 2)
        self.assertIn(self.chat_message1, messages)
        self.assertIn(self.chat_message2, messages)
        
class GetMessageTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a test message
        self.message = ChatMessage.objects.create(username=self.user, message='Test message')
        
    def test_get_message(self):
        # Authenticate the user
        self.client.login(username='testuser', password='testpassword')
        
        # Prepare the URL for the GET request
        url = reverse('getMessage')
        
        # Make the GET request with the message ID
        response = self.client.get(url, {'messageID': self.message.id})
        
        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        
        # Assert the response data
        data = response.json()
        self.assertEqual(data['username'], 'testuser')
        self.assertEqual(data['message'], 'Test message')

class UpdateMessageUpvotesTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a test user profile
        self.user_profile = UserProfile.objects.create(user=self.user)
        
        # Create a test message
        self.message = ChatMessage.objects.create(id=1, upvotes=0)
        
    def test_update_message_upvotes(self):
        # Authenticate the user
        self.client.login(username='testuser', password='testpassword')
        
        # Prepare the URL for the GET request
        url = reverse('updateMessageUpvotes')
        
        # Make the GET request with the message ID and new upvotes
        response = self.client.get(url, {'messageID': 1, 'newUpvotes': 10, 'isUpvote': 'true'})
        
        # Assert the response status code
        self.assertEqual(response.status_code, 200)
        
        # Refresh the message from the database
        self.message.refresh_from_db()
        
        # Assert the updated upvotes value
        self.assertEqual(self.message.upvotes, 10)
        
        # Assert the user profile relationship with the message
        self.assertEqual(self.user_profile.upvotedMessages.count(), 1)
        self.assertEqual(self.user_profile.upvotedMessages.first(), self.message)