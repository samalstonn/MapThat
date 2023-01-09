from django.urls import path

from . import views

app_name = 'mapthat'
urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('manual/', views.manual, name='manual'),
    path('upload/', views.upload, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('tutorial/', views.tutorial, name='tutorial'),
]
