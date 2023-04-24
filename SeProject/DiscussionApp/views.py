from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from MapApp.models import Poi
from .models import ChatMessage

# view to get the discussion history


@login_required
def viewDiscussion(request, aid):
    context = {}
    point = Poi.objects.get(id=aid)
    print("aid: " + str(aid))
    print("name: " + point.name)
    context['name'] = point.name
    context['aid'] = str(aid)
    messages = ChatMessage.objects.filter(chatroom=aid)
    context['messages'] = messages
    return render(request, 'DiscussionApp/discussion.html', context)


def sendMessage(request):
    if request.method == 'POST':
        message = request.POST['message']
        chat_message = ChatMessage(username=request.user, message=message)
        chat_message.save()
    return redirect('chat')
