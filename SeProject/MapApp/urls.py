from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name='map'), #main page goes to map app
    path('contact', views.contact, name='contact'), #contact page
    path('api/poi', views.apiCreatePoi, name="api_create_poi"), #create points of interest
    path('api/pois', views.apiPois, name="api_pois"), #points of interest
    path('privacy', views.privacy, name="privacy"), #privacy page
    path('assertations', views.assertations, name="assertations") #assertations page
]