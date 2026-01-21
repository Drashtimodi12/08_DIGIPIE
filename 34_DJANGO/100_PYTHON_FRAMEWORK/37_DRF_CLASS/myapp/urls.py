from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', ProductAPI.as_view())
]
