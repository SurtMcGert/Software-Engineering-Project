from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# sign up form class
class SignupForm(UserCreationForm):
 email = forms.EmailField(required=True, label='Email')
 class Meta:
    model = User
    fields = ("username", "email")

# change password form
class ChangePassForm(forms.Form):
    oldpw = forms.CharField(required=True,label="Old password:",widget=forms.PasswordInput())
    newpw = forms.CharField(required=True,label="New password:",widget=forms.PasswordInput())
    confirm = forms.CharField(required=True,label="Confirm password:",widget=forms.PasswordInput())
