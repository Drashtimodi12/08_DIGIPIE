from django.contrib import admin
from django.urls import path
from app9.views import *

urlpatterns = [
    path('', index, name='index'),
]
