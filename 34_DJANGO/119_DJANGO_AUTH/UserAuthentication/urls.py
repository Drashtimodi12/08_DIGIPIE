from django.urls import path
from UserAuthentication.views import *

urlpatterns = [
    path('', about, name='about'),
    path('loginpage', loginpage, name='loginpage'),
    path('reg', reg, name='reg'),
    path('adduser', adduser, name='adduser'),
    path('loginuser', loginuser, name='loginuser'),
    path('home', home, name='home'),

    path('admin_page', admin_page, name='admin_page'),
    path('staff_page', staff_page, name='staff_page'),

    path('logoutuser', logoutuser, name='logoutuser'),


]
