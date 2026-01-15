from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<a href='/about'>About</a> | <a href='/contact'>Contact</a> " \
    # "\n Hello, World! Welcome to my website. This is the index page. Please navigate to other pages to see the other functionalities. ")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')