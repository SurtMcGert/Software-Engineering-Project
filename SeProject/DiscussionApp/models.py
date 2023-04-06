from django.db import models
from django.contrib.auth.models import User

# Due to how the WebSocket works, each chat message is saved twice. As a workaround, the template displays only even-numbered messages
class ChatMessage(models.Model):
    username = models.TextField() # Taking an actual user requires implementation in routing.py
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
