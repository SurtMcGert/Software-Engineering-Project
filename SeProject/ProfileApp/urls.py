from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayProfile, name='displayProfile'), #main page displays user profile
    path('createProfile/<int:uid>', views.createProfile, name='createProfile'), #create a new profile
]