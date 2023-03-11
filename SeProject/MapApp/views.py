from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from .models import Poi

import requests

# view to render the map page
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

#view to return points of interest???
def api_pois(request):
    pois = list(Poi.objects.all().values('name', 'latitude', 'longitude'))
    print(pois)
    return JsonResponse(pois, safe=False)
