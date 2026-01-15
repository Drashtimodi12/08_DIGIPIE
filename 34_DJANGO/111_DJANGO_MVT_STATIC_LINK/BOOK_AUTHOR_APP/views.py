from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    # return HttpResponse("HEllo")
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html', {'title':'HOME'})

def contact(request):
    return render(request, 'contact.html')

