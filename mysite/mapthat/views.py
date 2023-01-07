from django.shortcuts import render
from django.http import request
from .forms import LoginForm,SignupForm,PasswordMatchError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms
from django.db.utils import IntegrityError

# Create your views here.

def home(request,context = {}):
    return render(request, 'mapthat/index.html',context)

def signup(request):
  if request.method == 'POST':
    signupform = SignupForm(request.POST)
    try:
      signupform.is_valid()
      signupform.clean()
      firstname = signupform.cleaned_data['firstname'].capitalize()
      lastname = signupform.cleaned_data['lastname'].capitalize()
      username = signupform.cleaned_data['username']
      email = signupform.cleaned_data['email']
      password = signupform.cleaned_data['password']
      user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,
      email=email)
      user.save()
      return login(request,context={'user':user})
    except forms.ValidationError as e:
      context = {
          'signupform': signupform,
          'error': True,
          'message': 'There is an Error'
          }
      if e.code == 'password_mismatch':
        context['message'] = 'Passwords do not match.'
      else:
        context['message'] = 'There is an Error'
      return render(request,'mapthat/signup.html',context)
    except IntegrityError as e:
      context = {
          'signupform': signupform,
          'error': True,
          'message': 'Username already exists. Please login or choose another username.'
          }
      return render(request,'mapthat/signup.html',context) 
  else:
    signupform = SignupForm()
  context = {
    'signupform': signupform,
    'error' : False
    }
  return render(request,'mapthat/signup.html',context)
  

def login(request,context={}):
  if context:
    return home(request,context)
  if request.method == 'POST':
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
      username = loginform.cleaned_data['username']
      password = loginform.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        firstname=User.objects.get(username=username).first_name
        return home(request,{'user':user})
      else:
        context = {
          'loginform': loginform,
          'error': True,
          'message': 'Invalid username or password'
          }
        return render(request,'mapthat/login.html',context)
  else:
    loginform=LoginForm()
  context = {
    'loginform': loginform,
    'error' : False
  }
  return render(request, 'mapthat/login.html',context)

    