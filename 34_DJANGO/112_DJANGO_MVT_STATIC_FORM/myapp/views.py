from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        context = {
            'name' : name,
            'email' : email,
            'password' : password
        }
        return render(request, 'success.html', context)
    return render(request, 'register.html')