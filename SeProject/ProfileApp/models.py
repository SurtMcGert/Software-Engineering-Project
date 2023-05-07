from django.db import models
from django.contrib.auth.models import User
from DiscussionApp.models import ChatMessage

# model for achievement badges
class Badge(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['name']), ]

        def __str__(self):
            return self.name


# model for user profiles
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False)
    badges = models.ManyToManyField(Badge, blank=True, null=True)
    upvotedMessages = models.ManyToManyField(ChatMessage, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        indexes = [models.Index(fields=['id']), ]

        def __str__(self):
            return str(self.id)
