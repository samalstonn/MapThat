from django.shortcuts import render
from django.http import request
from .forms import LoginForm, SignupForm, IconForm, MapForm, UploadForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms
from . import filemap
from .models import Map, colorchoices
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
        return home(request, context)
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


def map(request, map):
    context = {
        'map': map.get_root().render()
    }
    return render(request, 'mapthat/map_template.html', context)


def manual(request, context={}):
    return render(request, 'mapthat/manual.html', context)


attrib = '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'


def upload(request):
    if request.method == 'POST':
        uploadform = UploadForm(request.POST, request.FILES)
        mapform = MapForm(request.POST)
        iconform = IconForm(request.POST)
        if mapform.is_valid():
            currmap = Map.objects.create(
                name=mapform.cleaned_data['name'],
                location_latitude=mapform.cleaned_data['location_latitude'],
                location_longitude=mapform.cleaned_data['location_longitude'],
                zoom=mapform.cleaned_data['zoom'],
                tiles=mapform.cleaned_data['tiles'],
                attr=attrib
            )
            currmap.save()
        if uploadform.is_valid():
            if iconform.is_valid():
                icon = folium.Icon(color=iconform.cleaned_data['color'],
                                   icon_color=iconform.cleaned_data['icon_color'],
                                   icon=iconform.cleaned_data['icon'], angle=0, prefix='fa')
            newmap = filemap.makemapzip(
                request.FILES['file'], currmap.pk, icon)
        return map(request, newmap)
    else:
        mapform = MapForm()
        uploadform = UploadForm()
        iconform = IconForm()
    context = {
        'uploadform': uploadform,
        'mapform': mapform,
        'iconform': iconform
    }
    return render(request, "mapthat/upload.html", context)


def gallery(request, context={}):
    return render(request, 'mapthat/gallery.html', context)


def tutorial(request, context={}):
    return render(request, 'mapthat/tutorial.html', context)
