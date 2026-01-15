from django.shortcuts import render
from django.http import HttpResponse
from MiddlewareApp.models import *
# Create your views here.

def home(request):
    return HttpResponse("Hello")

def about(request):
    return render(request, 'index.html')