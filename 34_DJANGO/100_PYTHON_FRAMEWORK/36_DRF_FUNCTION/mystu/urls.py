from django.contrib import admin
from django.urls import path
from mystu.views import *

urlpatterns = [
    path('viewstu', viewstu, name='viewstu'),
    path('addstu', addstu, name='addstu'),
    path('updatestu/<int:id>', updatestu, name='updatestu'),
    path('deletestu/<int:id>', deletestu, name='deletestu')
]
