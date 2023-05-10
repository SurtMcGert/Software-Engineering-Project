from django.urls import path

from . import views

urlpatterns = [
    path('<int:aid>', views.viewDiscussion, name='loadDiscussionPage'), #load a discussion page
    path('sendMessage', views.sendMessage, name='sendMessage'), #send a message to a discussion page
    path('userUpvotedCheck', views.userUpvotedCheck.as_view(), name='userUpvotedCheck'),
    path('getMessage', views.getMessage.as_view(), name='getMessage'),
    path('updateMessageUpvotes', views.updateMessageUpvotes.as_view(), name='updateMessageUpvotes')
]
