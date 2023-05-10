# imports
import re
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import ChangePassForm, SignupForm


# class based view for signing up a user
class SignupUser(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_user_id(self):
        return self.request.user.id

    def post(self, request):
        # Create a new user
        user = User.objects.create_user(
            request.POST['username'], request.POST['email'], request.POST['password1'])

        # Get the id of the user that was just created
        id = user.id

        # Redirect the user to the login page
        return redirect(reverse_lazy('createProfile', kwargs={'uid': id}))

# view for changing a users password
@login_required
def changePassword(request):
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['newpw'] == form.cleaned_data['confirm']:
                usr = request.user
                check = authenticate(username=usr.username,
                                     password=form.cleaned_data['oldpw'])
                if check is None:
                    messages.add_message(
                        request, messages.ERROR, 'Incorrect password.')
                else:
                    if form.cleaned_data['oldpw'] == form.cleaned_data['newpw']:
                        messages.add_message(
                            request, messages.ERROR, 'New password cannot be the same as old password.')
                    else:
                        try:
                            validate = validate_password(
                                form.cleaned_data['newpw'], user=usr)
                            usr.set_password(form.cleaned_data['newpw'])
                            usr.save()
                            messages.add_message(
                                request, messages.SUCCESS, 'Your password has been changed.')
                            if 'next' in request.GET.keys():
                                return HttpResponseRedirect(request.GET['next'])
                            else:
                                return HttpResponseRedirect('/')
                        except ValidationError as e:
                            for i in e:
                                messages.add_message(
                                    request, messages.ERROR, i)
            else:
                messages.add_message(
                    request, messages.ERROR, 'Passwords do not match.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'An error occurred. Please try again.')
    # GET request
    context = {}
    form = ChangePassForm()
    context['form'] = form
    return render(request, 'registration/changePassword.html', context)

# view to delete a users account
@login_required
def deleteAccount(request):
    if request.method == 'POST':
        uid = request.user.id
        request.user.delete()
        logout(request)
        return redirect(reverse_lazy('deleteProfile', kwargs={'uid': uid}))
    else:
        return render(request, 'registration/deleteAccount.html')