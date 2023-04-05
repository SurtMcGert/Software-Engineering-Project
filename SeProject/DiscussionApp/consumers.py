import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


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

        await self.channel_layer.group_send(
                self.discussionGroupName, {
                    'type': 'chat_message',
                    'message': message,
                    'username' : username,
                    }
                )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            }))

    pass
