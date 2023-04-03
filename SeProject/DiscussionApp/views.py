from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.generic import View
from channels.generic.websocket import AsyncWebsocketConsumer

def viewDiscussion(self, request, aid):
    context = {}
    context['aid'] = aid
    return render(request, 'DiscussionApp/discussion.html', context)

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