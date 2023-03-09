from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('api/animals', views.api_animals, name="api_animals"),
    path('api/pois', views.api_pois, name="api_pois")
]