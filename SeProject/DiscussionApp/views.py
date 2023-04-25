from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from MapApp.models import Poi
from .models import ChatMessage
from django.views import View
from ProfileApp.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

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

# Returns True if user has upvoted this message
# Input 'userID' and 'messageID'
class userUpvotedCheck(LoginRequiredMixin, View):
    def get(self, request):
        userProfileID = request.GET.get('userID')
        messageID = request.GET.get('messageID')

        userProfile = UserProfile.objects.get(id=userProfileID)
        message = ChatMessage.objects.get(id=messageID)


        if userProfile.upvotedMessages.filter(id=messageID).exists():
            return JsonResponse({'success':True}, status=200)
        return JsonResponse({'success':False}, status=200)

# Returns a ChatMessage object
# Input 'messageID'
class getMessage(LoginRequiredMixin, View):
    def get(self, request):
        messageID =  request.GET.get('messageID')
        message = ChatMessage.objects.get(id=messageID)

        username = message.username
        messageContent = message.message
        created_at = message.created_at
        upvotes = message.upvotes
        if message.parentMessage!='null':
            parentMessage = message.parentMessage
        else:
            parentMessage = 'null'

        return JsonResponse({'username':username,
                             'message':messageContent,
                             'created_at':created_at,
                             'upvotes':upvotes,
                             'parentMessage':parentMessage}, status=200)


# Updates the number of upvotes a message has
# Input 'messageID' and 'newUpvotes'
class updateMessageUpvotes(LoginRequiredMixin, View):
    def get(self, request):
        messageID = request.GET.get('messageID')
        newUpvotes = request.GET.get('newUpvotes')

        message = ChatMessage.objects.get(id=messageID)
        message.upvotes = newUpvotes
        message.save()

        return JsonResponse({'success':True})
