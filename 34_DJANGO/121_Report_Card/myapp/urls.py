from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('marksheet', marksheet, name='marksheet'),
    path('sendmail', send_mail_page, name='send_mail_page'),
]
