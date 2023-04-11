from django.urls import path

from . import views

urlpatterns = [
    path('<int:aid>', views.viewDiscussion, name='loadDiscussionPage'), #load a discussion page
    path('sendMessage', views.sendMessage, name='sendMessage'),
]
