
from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("menu/", menu, name="menu"),
    path("menuimg/", menuimg, name="menuimg"),
]
