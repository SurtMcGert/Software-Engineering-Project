from django.shortcuts import render
import re
from django.contrib import messages
from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .models import Badge, UserProfile
from DiscussionApp.models import ChatMessage

# view to display a users profile


@login_required 
def displayProfile(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=user)
        checkAchievements(request)
        username = user.username
        badges = profile.badges.all()
        context['name'] = username
        context['badges'] = list(badges)
        return render(request, 'ProfileApp/userProfile.html', context)
    else:
        return redirect(reverse_lazy('login'))


# view to create a users profile
def createProfile(request, uid):
    user = get_object_or_404(User, id=uid)
    if UserProfile.objects.filter(user=user).exists():
        return
    profile = UserProfile.objects.create(user=user)
    profile.badges.add(get_object_or_404(Badge, name="welcome"))
    return redirect(reverse_lazy('login'))

# view to delete a users profile
def deleteProfile(request, uid):
    profiles = UserProfile.objects.filter(user__isnull=True)
    for profile in profiles:
        profile.delete()
    return redirect(reverse_lazy('map'))

#view to check to see which achievements a user should be awarded
@login_required
def checkAchievements(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    #communicate in your first discussion
    userMessages = ChatMessage.objects.filter(username=user.username)
    badge = get_object_or_404(Badge, name="making contact")
    hasAchievement = profile.badges.filter(id = badge.id).exists()
    if((len(userMessages) >= 1) & (not hasAchievement)):
        profile.badges.add(badge)
    
    #get upvotes on your messages
    badge = get_object_or_404(Badge, name="noticed?")
    hasAchievement = profile.badges.filter(id = badge.id).exists()
    maxUpvotes = 0
    for m in userMessages:
        if(m.upvotes > maxUpvotes):
            maxUpvotes = m.upvotes
    #five upvotes
    if((maxUpvotes >= 5) & (not hasAchievement)):
        profile.badges.add(badge)

    #50 upvotes
    badge = get_object_or_404(Badge, name="someone's popular")
    hasAchievement = profile.badges.filter(id = badge.id).exists()
    if((maxUpvotes >= 50) & (not hasAchievement)):
        profile.badges.add(badge)
    
    #100 upvotes
    badge = get_object_or_404(Badge, name="royalty")
    hasAchievement = profile.badges.filter(id = badge.id).exists()
    if((maxUpvotes >= 100) & (not hasAchievement)):
        profile.badges.add(badge)

    #replying to your first message
    badge = get_object_or_404(Badge, name="gossip")
    hasAchievement = profile.badges.filter(id = badge.id).exists()
    hasReplied = False
    for m in userMessages:
        if not m.parentMessage is None:
            hasReplied = True
            break

    if((hasReplied) & (not hasAchievement)):
        profile.badges.add(badge)