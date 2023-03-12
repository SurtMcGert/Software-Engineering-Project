from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'), #main page goes to map app
    path('login', views.sighin, name="login"), 
    path('api/animals', views.api_animals, name="api_animals"), #end point for animal api
    path('api/pois', views.api_pois, name="api_pois") #i have no idea
]