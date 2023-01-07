from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
    'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
    password = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password',
    'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))
  
class SignupForm(forms.Form):
  firstname = forms.CharField(max_length=100,
  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name',
  'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
  lastname = forms.CharField(max_length=100,
  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',
  'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
  username = forms.CharField(max_length=100,
  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
  'type': 'text', 'id': 'floatingInput', 'for': 'floatingInput'}))
  password = forms.CharField(max_length=100,
  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password',
  'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))
  repeatpassword = forms.CharField(max_length=100,
  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password',
  'type': 'password', 'id': 'floatingPassword', 'for': 'floatingPassword'}))
  email = forms.CharField(max_length=100,
  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',
  'type': 'email', 'id': 'floatingInput', 'for': 'floatingInput'}))
