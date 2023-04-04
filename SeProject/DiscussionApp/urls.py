from django.urls import path

from . import views

urlpatterns = [
    path('<int:aid>', views.viewDiscussion.as_view(), name='loadDiscussionPage'), #load a discussion page
]
