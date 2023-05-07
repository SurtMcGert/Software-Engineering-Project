from rest_framework import serializers
from MapApp.models import Poi
from django.contrib.auth.models import User
from DiscussionApp.models import DiscussionBoard, ChatMessage
from ProfileApp.models import Badge, UserProfile


# serializer for the Poi model
class PoiSerializer(serializers.ModelSerializer):
    class Meta:
       model = Poi
       fields = ("id", "name", "latitude", "longitude", "animal_name", "scientific_name", "locations", "feature", "slogan", "habitat")

# serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ("id", "username")

# serializer for the DiscussionBoard model
class DiscussionBoardSerializer(serializers.ModelSerializer):
    class Meta:
       model = DiscussionBoard
       fields = ("id", "poi")

# serializer for the ChatMessage model
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
       model = ChatMessage
       fields = ("id", "username", "created_at", "chatroom", "upvotes", "parentMessage")

# serializer for the Badge model
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Badge
       fields = ("id", "name", "description", "image")

# serializer for the UserProfile model
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
       model = UserProfile
       fields = ("id", "user", "badges", "upvotedMessages")