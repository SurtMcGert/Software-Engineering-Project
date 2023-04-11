import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.auth import AuthMiddlewareStack
from channels.db import database_sync_to_async
from .models import ChatMessage


class DiscussionConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("connecting")
        self.aid = self.scope['url_route']['kwargs']['aid']
        self.discussionGroupName = 'discussion%s' % self.aid
        
        await self.channel_layer.group_add(
                self.discussionGroupName,
                self.channel_name
                )
        await self.accept()
        
    async def disconnect(self, close_code):
        print("disconnect")
        await self.channel_layer.group_discard(
                self.discussionGroupName,
                self.channel_name
                )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await modelSave(username=username, message=message)

        await self.channel_layer.group_send(
                self.discussionGroupName, {
                    'type': 'chat_message',
                    'message': message,
                    'username' : username,
                    }
                )

    async def chat_message(self, event):
        username = event['username']
        message = event['message']


        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            }))

    pass

@database_sync_to_async
def modelSave(username, message):
    model = ChatMessage(username=username, message=message)
    model.save()
