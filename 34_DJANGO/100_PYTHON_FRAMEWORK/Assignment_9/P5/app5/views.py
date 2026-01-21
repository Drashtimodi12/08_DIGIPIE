from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        return HttpResponse(f"Thank You, {name}! We have received your email: {email}.")
    return render(request, 'index.html')