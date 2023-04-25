import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatMessage

# Handles streaming for the chatrooms
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
        isReply = False
        #if this message is a reply to another message
        try:
            replyID = text_data_json['replyID']
            isReply = True
            replyID = int(replyID)
        except KeyError:
            replyID = ''
        
        # Save message to model so they can be retrieved when the page is refreshed
        if isReply:
            newMessage = await modelSave(username=username, message=message, chatroom=self.aid, parentMessageID = replyID)
        else:
            newMessage = await modelSave(username=username, message=message, chatroom=self.aid)

        await self.channel_layer.group_send(
                self.discussionGroupName, {
                    'type': 'chat_message',
                    'message': message,
                    'username' : username,
                    'id' : newMessage.id,
                    'upvotes' : newMessage.upvotes,
                    'parentID': replyID,
                    }
                )

    async def chat_message(self, event):
        username = event['username']
        message = event['message']
        id = event['id']
        upvotes = event['upvotes']
        parentID = event['parentID']
        if (parentID == ''):
            parentID = -1


        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'id' : id,
            'upvotes' : upvotes,
            'parentID' : parentID,
            }))

    pass

# Asynchronous calls to the model is not allowed, so we need this function (notice the decorator)
@database_sync_to_async
def modelSave(username, message, chatroom, parentMessageID = -1):
    if(parentMessageID == -1):
        model = ChatMessage(username=username, message=message, chatroom=chatroom)
    else:
        #if this message is a reply to another message, get the message its replying to
        parent = ChatMessage.objects.get(id = parentMessageID)
        model = ChatMessage(username=username, message=message, chatroom=chatroom, parentMessage=parent)
    model.save()
    return model
