import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class DiscussionConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.aid = self.scope['url_route']['kwargs']['aid']
        self.discussionGroupName = 'discussion%s' % self.aid
        
        await self.channel_layer.group_add(
                self.discussionGroupName,
                self.channelName
                )

        await self.accept()
        
        await self.channel_layer.group_send(
                self.discussionGroupName,
                {
                    'type': 'tester_message',
                    'tester': 'Hello, World!',
                }
                )

        async def tester_message(self, event):
            tester = event['tester']
            await self.send(text_data=json.dumps({'tester': tester,}))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
                self.discussionGroupName,
                self.channelName
                )

    pass
