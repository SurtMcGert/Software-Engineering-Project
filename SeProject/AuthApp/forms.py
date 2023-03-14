from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#login form class
class LoginForm(forms.Form):
    #TODO - WRITE A LOGIN FORM
    temp = 1 #delete this, its only here to stop erroring because you cant have a class with nothing in it

# sign up form class
class SignupForm(UserCreationForm):
 email = forms.EmailField(required=True, label='Email')
 class Meta:
    model = User
    fields = ("username", "email")
