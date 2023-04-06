from channels.generic.websocket import AsyncWebsocketConsumer
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ChatMessage


def viewDiscussion(request, aid):
    context = {}
    context['aid'] = str(aid)
    messages = ChatMessage.objects.all()
    context['messages']= messages
    return render(request, 'DiscussionApp/discussion.html', context)

# I didn't even know this is used, but if you delete it, the whole chat system breaks
def sendMessage(request):
    if request.method=='POST':
        message = request.POST['message']
        chat_message = ChatMessage(user=request.user, message=message)
        chat_message.save()
    return redirect('chat')
