from django.urls import path

from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('api/animals', views.api_animals)
]