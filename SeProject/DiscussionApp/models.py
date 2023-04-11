from django.contrib.auth.models import User
from django.db import models
from MapApp.models import Pois


# Create your models here.
class DiscussionBoard(models.Model):
    poi = models.ForeignKey('Pois', on_delete=models.CASCADE) # The point of interest this discussion board is for
    subscribers = models.ManyToManyField('User') # Users who are subscribed to the posts on this board

class Post(models.Model): # A post in the discussion board
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.SET_NULL) # User who made the post
    text = models.TextField()
    image = models.FileField(upload_to="/upload/", null=True)
    points = models.IntegerField() # The number of times the post has been liked
    time = models.DateTimeField(auto_now_add=True) # Time posted
    reply = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True) # The post this is a reply to, if any
# Due to how the WebSocket works, each chat message is saved twice. As a workaround, the template displays only even-numbered messages
class ChatMessage(models.Model):
    username = models.TextField() # Taking an actual user requires implementation in routing.py
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
