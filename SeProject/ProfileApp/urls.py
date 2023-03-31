from django.urls import path
from . import views

urlpatterns = [
    # main page displays user profile
    path('', views.displayProfile, name='displayProfile'),
    path('createProfile/<int:uid>', views.createProfile,
         name='createProfile'),  # create a new profile
    path('deleteProfile/<int:uid>', views.deleteProfile,
         name='deleteProfile'),  # create a new profile
]
