from django.contrib import admin
from django.urls import path
from myemp.views import *

urlpatterns = [
    path('viewemp', viewemp, name='viewemp'),
    path('addemp', addemp, name='addemp'),
    path('updateemp/<int:id>', updateemp, name='updateemp'),
    path('deleteemp/<int:id>', deleteemp, name='deleteemp')
]
