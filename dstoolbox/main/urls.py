
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", menu_list, name='menu'),
    path("menu/add-to-cart/<int:menu_id>/", add_to_cart, name="add_to_cart"),
    path("view_menu_selected/", view_menu_selected, name="view_menu_selected"),
    path("test/", test, name='test'),
    # path("login/", user_login, name="login"),
    # # path("register/", register, name="register"),
    # # path("logout/", user_logout, name="logout"),
    # # path("menu/", menu, name="menu"),
    # # path("menuimg/", menuimg, name="menuimg"),
]
