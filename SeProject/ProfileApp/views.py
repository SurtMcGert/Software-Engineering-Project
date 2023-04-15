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

# view to display a users profile


@login_required 
def displayProfile(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=user)
        username = user.username
        badges = profile.badges
        context['name'] = username
        context['badges'] = badges
        return render(request, 'ProfileApp/userProfile.html', context)
    else:
        return redirect(reverse_lazy('login'))


# view to create a users profile
def createProfile(request, uid):
    user = get_object_or_404(User, id=uid)
    if UserProfile.objects.filter(user=user).exists():
        return
    profile = UserProfile.objects.create(user=user)
    return redirect(reverse_lazy('login'))

# view to delete a users profile
def deleteProfile(request, uid):
    profiles = UserProfile.objects.filter(user__isnull=True)
    for profile in profiles:
        profile.delete()
    return redirect(reverse_lazy('map'))
