from django.contrib import admin
from django.urls import path
from ajax.views import *
from ajaxcrud import views

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('countries', countries, name='countries'),
    path('states', states, name='states'),
    path('cities', cities, name='cities'),
    path('ajaxcrud', views.home, name='ajaxcrud'),  # CRUD AJAX view
]
