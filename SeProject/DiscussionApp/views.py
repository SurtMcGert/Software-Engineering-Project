from django.shortcuts import redirect, render

from .models import ChatMessage

#view to get the discussion history
def viewDiscussion(request, aid):
    context = {}
    context['aid'] = str(aid)
    messages = ChatMessage.objects.filter(chatroom=aid)
    context['messages'] = messages
    return render(request, 'DiscussionApp/discussion.html', context)

def sendMessage(request):
    if request.method=='POST':
        message = request.POST['message']
        chat_message = ChatMessage(username=request.user, message=message)
        chat_message.save()
    return redirect('chat')
