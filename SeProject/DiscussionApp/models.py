from django.contrib.auth.models import User
from django.db import models

from MapApp.models import Poi


# Create your models here.
class DiscussionBoard(models.Model):
    poi = models.ForeignKey(Poi, on_delete=models.CASCADE) # The point of interest this discussion board is for
    subscribers = models.ManyToManyField(User) # Users who are subscribed to the posts on this board

# class Post(models.Model): # A post in the discussion board
#     thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL) # User who made the post
#     text = models.TextField()
#     image = models.FileField(upload_to="/upload/", null=True)
#     points = models.IntegerField() # The number of times the post has been liked
#     time = models.DateTimeField(auto_now_add=True) # Time posted
#     reply = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True) # The post this is a reply to, if any

# A single chat messages
class ChatMessage(models.Model):
    username = models.TextField() # Taking an actual user requires implementation in routing.py
    message = models.TextField() # The text content of the message
    created_at = models.DateTimeField(auto_now_add=True) # the time of message creation
    chatroom = models.IntegerField(blank=False, null = True) # The chatroom it was sent in
    upvotes = models.IntegerField(default=0) # the number of upvotes on a message
    parentMessage = models.ForeignKey('self', on_delete=models.CASCADE, null=True) # the parent that this message is a reply to

#    def __str__(self):
#        return self.message
