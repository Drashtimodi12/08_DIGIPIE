from django.contrib import admin
from django.urls import path
from doctor12.views import *

urlpatterns = [
    path('', index, name='index')
]
