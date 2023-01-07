from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def home(request,context = {}):
    return render(request, 'mapthat/index.html',context)

def signup(request):
  if request.method == 'POST':
    signupform = SignupForm(request.POST)
    if signupform.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      user = User.objects.create_user(username,email,password)
      user.save()
      return home(request,{'user':username})
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
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        return home(request,{'user':username})
  else:
    loginform=LoginForm()
  context = {
    'loginform': loginform
  }
  return render(request, 'mapthat/login.html',context)

    