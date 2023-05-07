from django.shortcuts import render
from rest_framework import viewsets

from RestAPI.serializers import PoiSerializer, UserSerializer, DiscussionBoardSerializer, ChatMessageSerializer, BadgeSerializer, UserProfileSerializer
from MapApp.models import Poi
from django.contrib.auth.models import User
from DiscussionApp.models import DiscussionBoard, ChatMessage
from ProfileApp.models import Badge, UserProfile

#view set for the Poi restAPI access
class PoiViewSet(viewsets.ModelViewSet):
   queryset = Poi.objects.all()
   serializer_class = PoiSerializer


#view set for the User restAPI access
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

#view set for the DiscussionBoard restAPI access
class DiscussionBoardViewSet(viewsets.ModelViewSet):
   queryset = DiscussionBoard.objects.all()
   serializer_class = DiscussionBoardSerializer

#view set for the ChatMessage restAPI access
class ChatMessageViewSet(viewsets.ModelViewSet):
   queryset = ChatMessage.objects.all()
   serializer_class = ChatMessageSerializer

#view set for the Badge restAPI access
class BadgeViewSet(viewsets.ModelViewSet):
   queryset = Badge.objects.all()
   serializer_class = BadgeSerializer

#view set for the UserProfile restAPI access
class UserProfileViewSet(viewsets.ModelViewSet):
   queryset = UserProfile.objects.all()
   serializer_class = UserProfileSerializer