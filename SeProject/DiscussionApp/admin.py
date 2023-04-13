from django.contrib import admin
from .models import ChatMessage, DiscussionBoard

# Register your models here.
admin.site.register(ChatMessage)
admin.site.register(DiscussionBoard)