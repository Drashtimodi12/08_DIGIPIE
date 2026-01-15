from django.urls import path
from Student_CRUD.views import *

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('update', update, name='updatestu'),
    path('delete', delete, name='deletestu')
]
