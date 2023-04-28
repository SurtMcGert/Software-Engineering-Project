from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from .models import Poi

import requests

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
def apiCreatePoi(request):
    if "name" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "latitude" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "longitude" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if len(request.FILES) != 1 or "image" not in request.FILES:
        return HttpResponse(status=requests.codes.bad)

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

    poi = Poi(
        name=animal_info["name"],
        latitude=request.POST.get("latitude"),
        longitude=request.POST.get("longitude"),
        scientific_name=animal_info["taxonomy"]["scientific_name"],
        locations=", ".join(animal_info["locations"]),
        feature=animal_info["characteristics"]["distinctive_feature"],
        slogan=animal_info["characteristics"]["slogan"],
        habitat="null",
        image=request.FILES["image"]
    )
    poi.save()
    return JsonResponse(poi.to_json(), safe=False)

# Accessed at /api/pois
# Returns all of the POIs
@require_GET
def apiPois(request):
    pois = [p.to_json() for p in Poi.objects.all()]
    return JsonResponse(pois, safe=False)


# view to view the privacy page
def privacy(request):
    context = {}
    return render(request, 'privacy.html', context)

#view to view the assertations page
def assertations(request):
    context = {}
    return render(request, 'assertations.html', context)
