from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('countries', countries, name='countries'),
    path('states', states, name='states'),
    path('cities', cities, name='cities')
]
