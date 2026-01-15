from django.urls import path
from Visitor_App.views import *

urlpatterns = [
    path('', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout, name='logout'),
]
