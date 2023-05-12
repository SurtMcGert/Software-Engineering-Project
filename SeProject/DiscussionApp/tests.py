from django.test import TestCase
from django.contrib.auth.models import User
from DiscussionApp.models import ChatMessage
from ProfileApp.models import UserProfile
from django.test.client import Client

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
