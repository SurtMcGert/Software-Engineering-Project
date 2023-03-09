from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

import requests

def map(request):
    key = settings.GOOGLE_MAPS_KEY
    context = {
        'key': key
    }

    return render(request, 'map.html', context)

def api_animals(request):
    response = requests.get(
        f"https://api.api-ninjas.com/v1/animals?{request.GET.urlencode()}",
        headers={'X-Api-Key': settings.NINJA_API_KEY}
    )

    if response.status_code == requests.codes.ok:
        return HttpResponse(response.text)
    else:
        return HttpResponse("something is broken")
