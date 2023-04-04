from django.db import models

from MapApp.models import Pois
from django.contrib.auth.models import User

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
