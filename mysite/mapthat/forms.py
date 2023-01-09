from django import forms
from django.contrib.auth.models import User


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
