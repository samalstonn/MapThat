from django import forms
from django.contrib.auth.models import User
from .models import Map, colorchoices


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
                                                             'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
    password = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password',
                                                             'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))


class PasswordMatchError(forms.ValidationError):
    """
    Exception raised when passwords do not match
    """

    def __init__(self, message="Passwords do not match"):
        self.message = message
        super().__init__(self.message)


class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',
                                                              'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
    lastname = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',
                                                             'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
                                                             'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
    email = forms.CharField(max_length=100, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',
                                                          'type': 'email', 'id': 'floatingInput', 'for': 'floatingInput'}))
    password = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password',
                                                             'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))
    confirmpassword = forms.CharField(max_length=100, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password',
                                                                    'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))

    def clean(self):
        cleaned_data = super(forms.Form, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmpassword")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirmpassword does not match",
                code='password_mismatch',
            )


jawg_sunny = 'https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token=NNdSw2xyKpeRRVkxyW5H3FDsS9bmZfT8HQUCPmc9inyy5aRHEQyf20H4pTeCGBbK'
map_choices = [
    (jawg_sunny, 'Jawg Sunny'),
    ('Stamen Terrain', 'Stamen Terrain'), ('Stamen Toner', 'Stamen Toner'),
    ('Stamen Watercolor', 'Stamen Watercolor'), ('CartoDB positron', 'CartoDB positron')
]


class MapForm(forms.Form):
    name = forms.CharField(label='Map Name', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Your Map\'s Name'}))
    location_latitude = forms.FloatField(label='Latitude (Map Center)', required=False,
                                         initial=37.8283)
    location_longitude = forms.FloatField(label='Longitude (Map Center)', required=False,
                                          initial=-95.5795)
    zoom = forms.FloatField(label='Zoom', required=False, initial=4.5)
    tiles = forms.ChoiceField(label='Map Tiles (Background)', initial=jawg_sunny,
                              choices=map_choices)


class MarkerForm(forms.Form):
    latitude = forms.FloatField(label='Latitude',
                                widget=forms.TextInput(attrs={'placeholder': 42.447373}))
    longitude = forms.FloatField(label='Longitude',
                                 widget=forms.TextInput(attrs={'placeholder': -76.483703}))
    color = forms.ChoiceField(
        label='Color', initial='red', choices=colorchoices)
    popup = forms.CharField(label='Popup', required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Cornell University'}))
    tooltip = forms.CharField(label='Tooltip', required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Go Big Red!'}))


class IconForm(forms.Form):
    icon = forms.CharField(label='Icon', required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'fa-bank'}))
    icon_color = forms.ChoiceField(
        label='Icon Color', initial='white', choices=colorchoices)


class CircleForm(forms.Form):
    radius = forms.FloatField(label='Radius',
                              widget=forms.TextInput(attrs={'placeholder': 3}))
    outline = forms.ChoiceField(
        label='Outline Color', initial='red', choices=colorchoices)
    fill = forms.ChoiceField(
        label='Fill Color', initial='red', choices=colorchoices)
    opacity = forms.FloatField(label='Opacity', initial=0.5,
                               widget=forms.TextInput(attrs={'placeholder': 0.5}))


class KeyForm(forms.Form):
    # def __init__(self, newchoices, *args, **kwargs):
    #     super(KeyForm, self).__init__(*args, **kwargs)
    #     self.fields['tooltip'] = forms.ChoiceField(
    #         choices=newchoices)

    tooltip = forms.ChoiceField(label='Popup',
                                choices=[('red', 'red'), ('blue', 'blue')], initial='red')
    color = forms.ChoiceField(
        label='Color', initial='red', choices=colorchoices)


class UploadForm(forms.Form):
    file = forms.FileField(label='Upload a .xlsx file')
    type = forms.ChoiceField(label='Type', choices=[(
        'zipcode', 'Zipcode'), ('latlong', 'Latitude/Longitude')])
