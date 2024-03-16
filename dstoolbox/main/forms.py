from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    username = forms.CharField(label="", max_length=300, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Name'}))
    password1 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password Confirm'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        