from django.shortcuts import render
from app14.models import *

# Create your views here.

def index(request):
    doctors  = Doctor.objects.all()
    return render(request, 'index.html', {'doctors': doctors })
