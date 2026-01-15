from django.urls import path
from BOOK_AUTHOR_APP.views import *

urlpatterns = [
    path('', about, name='about'),
    path('home', home, name='home'),
    path('contact', contact, name='contact'),
]
