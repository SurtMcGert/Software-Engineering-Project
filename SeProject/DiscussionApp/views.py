from channels.generic.websocket import AsyncWebsocketConsumer
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Chat, Discussion


def viewDiscussion(request, aid):
    context = {}
    context['aid'] = aid
    return render(request, 'DiscussionApp/discussion.html', context)

# class viewDiscussion(View):
#     def get(self, request, **kwargs):
#         context = {}
#         template = 'DiscussionApp/discussion.html'
        
#         discussionID = self.kwargs['aid']
#         discussion = Discussion.objects.get(id=discussionID)
#         chats = Chat.objects.filter(discussion=discussionID)

#         context = {'messages': chats}
#         return render(request, template, context)

# class ChatConsumer(AsyncWebsocketConsumer):
#     def connect(self, event):
#         self.aid = event['aid']
#         self.room = self.channel_layer.group_get(self.aid)

#     def disconnect(self, event):
#         self.room.leave(self.aid)

#     def receive(self, text_data):
#         message = text_data.decode('utf-8')
#         self.room.send(text_data)

#     def send(self, text_data):
#         self.room.send(text_data)
