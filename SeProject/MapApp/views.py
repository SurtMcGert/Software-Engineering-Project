from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

import requests

# Home page
def map(request):
    key = settings.GOOGLE_MAPS_KEY
    context = {
        'key': key
    }

    return render(request, 'map.html', context)

# Accessed at /api/animals
# Forwards any query parameters to the Ninja Animals API
# Returns a text JSON response
def api_animals(request):
    response = requests.get(
        f"https://api.api-ninjas.com/v1/animals?{request.GET.urlencode()}",
        headers={'X-Api-Key': settings.NINJA_API_KEY}
    )

    if response.status_code == requests.codes.ok:
        return HttpResponse(response.text)
    else:
        return HttpResponse("something is broken")
