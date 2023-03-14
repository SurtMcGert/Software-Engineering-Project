from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.SignupUser.as_view(), name="signup"), #signup page
        # path('login', views.login, name="login"), #login page
        path('changepw', views.changepw, name='changepw'), #change password
        path('logout', views.logout, name='logout'), #logout
]
