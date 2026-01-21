from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("register", register, name="register"),
    path("adduser", adduser, name="adduser"),
    path("loginuser", loginuser, name="loginuser"),
    path("home", home, name="home"),
    path("userlogout", userlogout, name="userlogout"),
]
