from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', about, name='about'),
    path('index', index, name='index'),
]
