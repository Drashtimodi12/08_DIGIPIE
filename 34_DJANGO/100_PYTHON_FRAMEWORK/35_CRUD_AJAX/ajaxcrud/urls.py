from django.contrib import admin
from django.urls import path
from ajaxcrud.views import *

urlpatterns = [
    path('', home, name='home'),
    path('addstu', addstu, name='addstu'),
    path('fetchStudents', fetchStudents, name='fetchStudents'),
    path('deletedata', deletedata, name='deletedata'),
    path('databyid', databyid, name='databyid'),
    path('updatedata', updatedata, name='updatedata'),
    path('searchdata', searchdata, name='searchdata'),
]