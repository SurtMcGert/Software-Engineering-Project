#imports
import re

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import ChangePassForm, SignupForm


#class based view for signing up a user
class SignupUser(CreateView):
 model = User
 form_class = SignupForm
 template_name = 'registration/signup.html'
 success_url = reverse_lazy('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['newpw'] == form.cleaned_data['confirm']:
                usr = request.user
                check = authenticate(username=usr.username, password=form.cleaned_data['oldpw'])
                if check is None:
                   messages.add_message(request, messages.ERROR, 'Incorrect password.')
                else:
                  usr.set_password(form.cleaned_data['newpw'])
                  messages.add_message(request, messages.SUCCESS, 'Your password has been changed.')
                  return HttpResponseRedirect(reverse(index))
            else:
                messages.add_message(request, messages.ERROR, 'Passwords do not match.')
        else:
            messages.add_message(request, messages.ERROR, 'An error occurred. Please try again.')
    context = {}
    form = ChangePassForm()
    context['form'] = form
    return render(request, 'registration/change_password.html', context)

# def signup(request):
    
#     # Make POST requests in the format "/auth/createuser?fail=<url>&success=<url>"

#     # Can be used to redirect to a desired page after auth
#     if 'fail' in request.GET.keys():
#         fail = request.GET['fail']
#     else:
#         fail = '/'
#     if 'success' in request.GET.keys():
#         success = request.GET['success']
#     else:
#         success = '/'
    
#     if request.method == 'POST':
#         # Validation
#         if request.POST['password'] != request.POST['confirm']: 
#             messages.add_message(request, messages.ERROR, 'Passwords do not match.')
#             return HttpResponseRedirect(fail)
#         if User.objects.get(username = request.POST['username']) != None:
#             messages.add_message(request, messages.ERROR, 'Username already in use.')
#             return HttpResponseRedirect(fail)
#         if User.objects.get(email = request.POST['email']) != None:
#             messages.add_message(request, messages.ERROR, 'Email already in use.')
#             return HttpResponseRedirect(fail)
#         sym = re.search(r"[^a-zA-Z0-9_]", request.POST['username']) # Usernames can only contain letters, numbers or underscores
#         if sym is not None: 
#             messages.add_message(request, messages.ERROR, 'Username contains disallowed characters.')
#             return HttpResponseRedirect(fail)
#         email = re.search(r"\w+@\w+\.\w+", request.POST['email']) # Check email format
#         if email is None: 
#             messages.add_message(request, messages.ERROR, 'Please input a valid email address.')
#             return HttpResponseRedirect(fail)
            
#         # Create the user
#         usr = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
#         if usr == None: # Some error occurred
#             messages.add_message(request, messages.ERROR, 'An error occurred. Please try again.')
#             return HttpResponseRedirect(fail)
#         else: # Success
#             messages.add_message(request, messages.SUCCESS, 'Signed up successfully.')
#             login(request, usr)
#             return HttpResponseRedirect(success)
#     else: # In case of a GET request
#         return HttpResponseRedirect(fail)

# def login(request):
    
#     # Make POST requests in the format '/auth/login?fail=<url>&success=<url>
    
#     if 'fail' in request.GET.keys():
#         fail = request.GET['fail']
#     else:
#         fail = '/'
#     if 'success' in request.GET.keys():
#         success = request.GET['success']
#     else:
#         success = '/' 

#     if request.method == 'POST':      
#         usr = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if usr is None:
#             messages.add_message(request, messages.ERROR, 'Incorrect login.')
#             return HttpResponseRedirect(fail)
#         else:
#             messages.add_message(request, messages.SUCCESS, 'Logged in as ' + usr.username)
#             login(request, usr)
#             return HttpResponseRedirect(success)
#     else:
#         return HttpResponseRedirect(fail)

# @login_required
# def changepw(request):

#     # Make POST requests in the format '/auth/changepw?fail=<url>&success=<url>

#     if 'fail' in request.GET.keys():
#         fail = request.GET['fail']
#     else:
#         fail = '/'
#     if 'success' in request.GET.keys():
#         success = request.GET['success']
#     else:
#         success = '/' 

#     if request.method == 'POST':
#         usr = request.user
#         check = authenticate(username=usr.username, password=request.POST['oldpw'])
#         if check is None:
#             messages.add_message(request, messages.ERROR, 'Incorrect password.')
#             return HttpResponseRedirect(fail)
#         else:
#             usr.set_password(request.POST['newpw'])
#             messages.add_message(request, messages.SUCCESS, 'Your password has been changed.')
#             return HttpResponseRedirect(success)
#     else:
#         return HttpResponseRedirect(fail)

# @login_required
# def logout(request):

#     # Make POST requests in the format '/auth/logout?redir=<url>

#     logout(request)
#     messages.add_message(request, messages.SUCCESS, 'Logged out successfully.')
#     if 'redir' in request.GET.keys():
#         return HttpResponseRedirect(request.get['redir'])
#     else:
#         return HttpResponseRedirect('/')


