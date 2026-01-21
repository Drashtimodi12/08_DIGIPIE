from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        return HttpResponse(f"Received: Name={name}, Age={age}, Email={email}")
    return render(request, 'index.html')