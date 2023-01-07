from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.

def home(request):
    return render(request, 'mapthat/index.html')

def signup(request):
    return render(request, 'mapthat/signup.html')

def login(request):
  if request.method == 'POST':
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      return home(request)
  else:
    loginform=LoginForm()
  context = {
    'loginform': loginform
  }
  return render(request, 'mapthat/login.html',context)

    