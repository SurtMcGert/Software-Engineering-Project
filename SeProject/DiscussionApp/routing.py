from django.urls import re_path
from . import consumers

websocketURLPatterns = [
    re_path(r'wss/discussion/(?P<aid>\w+)/$', consumers.DiscussionConsumer.as_asgi(), name="wsDiscussion"),
]
