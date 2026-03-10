from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
import os
from myapp.models import *
from myapp.serializer import *

# Create your views here.

def about(request):
    return render(request, 'myapp/about.html')

def index(request):
    return render(request, 'myapp/index.html')