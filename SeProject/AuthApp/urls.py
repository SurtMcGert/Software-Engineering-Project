from django.urls import path
from . import views

urlpatterns = [
        path('createuser', views.createuser, name="createuser"),
        path('login', views.login, name="login"),
        path('changepw', views.changepw, name='changepw'),
        path('logout', views.logout, name='logout'),
]
