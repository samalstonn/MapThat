from django.shortcuts import render, redirect
from django.http import request
from .forms import LoginForm, SignupForm, IconForm, MapForm, UploadForm, KeyForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms
from . import filemap
from .models import Map, Icon
from django.db.utils import IntegrityError
from .makemap import makemap
import folium

# Create your views here.


def home(request, context={}):
    return render(request, 'mapthat/index.html', context)


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
            user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname,
                                            email=email)
            user.save()
            return login(request, context={'user': user})
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
            return render(request, 'mapthat/signup.html', context)
        except IntegrityError as e:
            context = {
                'signupform': signupform,
                'error': True,
                'message': 'Username already exists. Please login or choose another username.'
            }
            return render(request, 'mapthat/signup.html', context)
    else:
        signupform = SignupForm()
    context = {
        'signupform': signupform,
        'error': False
    }
    return render(request, 'mapthat/signup.html', context)


def login(request, context={}):
    if context:
        return redirect('home')
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                firstname = User.objects.get(username=username).first_name
                return home(request, {'user': user})
            else:
                context = {
                    'loginform': loginform,
                    'error': True,
                    'message': 'Invalid username or password'
                }
                return render(request, 'mapthat/login.html', context)
    else:
        loginform = LoginForm()
    context = {
        'loginform': loginform,
        'error': False
    }
    return render(request, 'mapthat/login.html', context)


def project(request, m):
    context = {
        'm': m.get_root().render()
    }
    return render(request, 'mapthat/map_template.html', context)


def manual(request, context={}):
    return render(request, 'mapthat/manual.html', context)


def key(request, mappk, choices):
    if request.method == 'POST':
        keyform = KeyForm(request.POST)
        if keyform.is_valid():
            key = keyform.cleaned_data['key']
            return project(request, makemap(map, key))
    else:
        keyform = KeyForm([('green', 'Green')])
    context = {
        'keyform': keyform,
    }
    return render(request, 'mapthat/key.html', context)


attrib = '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'


def upload(request):

    if request.method == 'POST':
        mapform = MapForm(request.POST)
        if mapform.is_valid():
            currmap = Map.objects.create(
                name=mapform.cleaned_data['name'],
                location_latitude=mapform.cleaned_data['location_latitude'],
                location_longitude=mapform.cleaned_data['location_longitude'],
                zoom=mapform.cleaned_data['zoom'],
                tiles=mapform.cleaned_data['tiles'],
                attr=attrib
            )
        uploadform = UploadForm(request.POST, request.FILES)
        if uploadform.is_valid():
            choices = filemap.get_choices_zip(request.FILES['file'])
        return key(request, currmap.pk, choices)

    else:
        mapform = MapForm()
        uploadform = UploadForm()
    context = {
        'uploadform': uploadform,
        'mapform': mapform,
    }
    return render(request, "mapthat/upload.html", context)


def gallery(request, context={}):
    return render(request, 'mapthat/gallery.html', context)


def tutorial(request, context={}):
    return render(request, 'mapthat/tutorial.html', context)
