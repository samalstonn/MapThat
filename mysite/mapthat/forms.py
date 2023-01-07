from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
    'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
    password = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password',
    'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))
  