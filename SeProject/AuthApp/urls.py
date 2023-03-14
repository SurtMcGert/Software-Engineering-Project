from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.SignupUser.as_view(), name="signup"), #signup page
        # path('changepw', views.changepw, name='changepw'), #change password
        # path('logout', views.logout, name='logout'), #logout
]
