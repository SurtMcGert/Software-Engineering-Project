from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'), #main page goes to map app
    path('api/poi', views.api_create_poi, name="api_create_poi"),
    path('api/pois', views.api_pois, name="api_pois") #i have no idea
]