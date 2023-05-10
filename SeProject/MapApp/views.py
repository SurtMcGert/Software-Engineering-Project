from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from .models import Poi
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse

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
# Requires a 'name', 'animal_name', 'latitude', and 'longitude' in the body
@require_POST
@csrf_exempt # TODO: Remove once in production
def apiCreatePoi(request):
    if "name" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "animal_name" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "latitude" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if "longitude" not in request.POST:
        return HttpResponse(status=requests.codes.bad)
    if len(request.FILES) != 1 or "image" not in request.FILES:
        return HttpResponse(status=requests.codes.bad)

    animal_info = requests.get(
        f"https://api.api-ninjas.com/v1/animals?name={request.POST.get('animal_name')}",
        headers={'X-Api-Key': settings.NINJA_API_KEY}
    )

    if animal_info.status_code != requests.codes.ok:
        return HttpResponse(status=requests.codes.bad)

    animal_info = animal_info.json()

    if len(animal_info) == 0:
        return HttpResponse(status=requests.codes.bad)
    
    animal_info = animal_info[0]

    poi = Poi(
        name=request.POST.get("name"),
        animal_name=animal_info["name"],
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

#view to render the contact page
def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = name + ':\n' + form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['wildWorld@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect(reverse('map'))

    return render(request, 'contact.html', {"form": form})