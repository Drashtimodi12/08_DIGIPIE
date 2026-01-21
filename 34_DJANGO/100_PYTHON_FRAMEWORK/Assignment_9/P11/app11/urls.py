from django.contrib import admin
from django.urls import path
from app11.views import *


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('edit', edit, name='edit'),
    path('delete', delete, name='delete'),
]
