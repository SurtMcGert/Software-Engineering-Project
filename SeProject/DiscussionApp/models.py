from django.db import models
from django.contrib.auth.models import User
from MapApp.models import Poi


# Each POI has a discussion page
class Discussion(models.Model):
    poi = models.ForeignKey(Poi, on_delete=models.CASCADE)


# Each discussion has a series of chat messages
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=512, blank=False)

    def __str__(self):
        return self.user.username

