from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Poi

import requests
import json

# view to render the map page
def map(request):
    key = settings.GOOGLE_MAPS_KEY
    context = {
        'key': key
    }

    return render(request, 'map.html', context)

# Accessed at /api/poi with a POST request
# Creates a new POI
# Fetches information about the POI from the Ninja Animals API
# Requires a 'name', 'latitude', and 'longitude' in the body
@require_POST
@csrf_exempt # TODO: Remove once in production
def api_create_poi(request):
    if "name" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "latitude" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "longitude" not in request.POST:
        return HttpResponse(statust=requests.codes.bad)

    animal_info = requests.get(
        f"https://api.api-ninjas.com/v1/animals?name={request.POST.get('name')}",
        headers={'X-Api-Key': settings.NINJA_API_KEY}
    )

    if animal_info.status_code != requests.codes.ok:
        return HttpResponse(status=requests.codes.bad)

    animal_info = animal_info.json()

    if len(animal_info) == 0:
        return HttpResponse(status=requests.codes.bad)
    
    animal_info = animal_info[0]

    poi = Poi.objects.create(
        name=animal_info["name"],
        latitude=request.POST.get("latitude"),
        longitude=request.POST.get("longitude"),
        scientific_name=animal_info["taxonomy"]["scientific_name"],
        locations=", ".join(animal_info["locations"]),
        feature=animal_info["characteristics"]["distinctive_feature"],
        slogan=animal_info["characteristics"]["slogan"],
        habitat="null"
    )
    poi.save()
    return JsonResponse(model_to_dict(poi), safe=False)

# Accessed at /api/pois
# Returns all of the POIs
@require_GET
def api_pois(request):
    pois = list(Poi.objects.all().values())
    return JsonResponse(pois, safe=False)
