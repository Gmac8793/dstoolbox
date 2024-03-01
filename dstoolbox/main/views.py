from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from .forms import *

def index(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def menuimg(request):
    return render(request, "menuimg.html")


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome to our shop.")
                redirect('main')
            else:
                messages.error(request, "Something went wrong!")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
            

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            #create profile
            Profile.objects.create(user=user, id_user=user.id)
            messages.success(request, "Register successfully!")
            return redirect('index')
        else:
            form = RegisterForm()
            
    return render(request, "register.html", {'form': form})


def logout(request):
    logout(request)
    messages.success(request, "ํYou are logged out.")