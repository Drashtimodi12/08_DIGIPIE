from django.shortcuts import render
from django.http import HttpResponse
from app13.models import *

# Create your views here.

def index(request):
    stu = Student.objects.all()
    return render(request, 'index.html', {'students' : stu})

