from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignupUser.as_view(), name="signup"),  # signup page
    path('changePassword', views.changePassword,
         name='changePassword'),  # change password
    path('deleteAccount', views.deleteAccount,
         name='deleteAccount'),  # delete user
]
