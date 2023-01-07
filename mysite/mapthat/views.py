from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import time

# Create your views here.

def home(request,context = {}):
    return render(request, 'mapthat/index.html',context)

def signup(request):
  if request.method == 'POST':
    signupform = SignupForm(request.POST)
    if signupform.is_valid():
      firstname = signupform.cleaned_data['firstname']
      lastname = signupform.cleaned_data['lastname']
      username = signupform.cleaned_data['username']
      email = signupform.cleaned_data['email']
      password = signupform.cleaned_data['password']
      user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,
      email=email)
      user.save()
      return home(request,{'firstname':firstname,'email':email})
  else:
    signupform=SignupForm()
  context = {
    'signupform': signupform
  } 
  return render(request, 'mapthat/signup.html',context)

def login(request):
  if request.method == 'POST':
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
      username = loginform.cleaned_data['username']
      password = loginform.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        firstname=User.objects.get(username=username).first_name
        return home(request,{'user':username,'firstname':firstname})
  else:
    loginform=LoginForm()
  context = {
    'loginform': loginform
  }
  return render(request, 'mapthat/login.html',context)

    