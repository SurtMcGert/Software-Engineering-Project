from channels.generic.websocket import AsyncWebsocketConsumer
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.generic import View


def viewDiscussion(request, aid):
    context = {}
    context['aid'] = str(aid)
    return render(request, 'DiscussionApp/discussion.html', context)
