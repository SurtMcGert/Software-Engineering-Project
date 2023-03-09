from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def map(request):
    key = settings.GOOGLE_MAPS_KEY
    context = {
        'key': key
    }

    return render(request, 'map.html', context)
