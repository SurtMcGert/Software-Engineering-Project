from django.urls import path

from . import views

urlpatterns = [
        path('signup', views.SignupUser.as_view(), name="signup"), #signup page
        path('change_password', views.change_password, name='change_password'), #change password
        path('delete_account', views.delete_account, name='delete_account'),
        # path('logout', views.logout, name='logout'), #logout
]
