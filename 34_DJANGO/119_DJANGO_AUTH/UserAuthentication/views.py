from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from UserAuthentication.models import *

# Create your views here.
def about(request):
    if request.user.id is None:
        return render(request, 'about.html')
    else:
        return redirect('home')

def loginpage(request):
    if request.user.id is None:
        return render(request, 'loginpage.html')
    else:
        return redirect('home')

def reg(request):
    if request.user.id is None:
        return render(request, 'reg.html')
    else:
        return redirect('home')

def adduser(request):
    try:
        if request.method=='POST':
            data = request.POST
            fname = data.get('fname')
            lname = data.get('lname')
            uname = data.get('uname')
            password = data.get('pass')

            if User.objects.filter(username=uname).exists():
                messages.add_message(request, messages.ERROR, "User Already Exist !!!!")
                return render(request,'reg.html')
            
            user = User(
                first_name=fname,
                last_name=lname,
                username=uname
            )
            user.set_password(password)
            user.save()

            messages.add_message(request, messages.SUCCESS, "Registration successfully")
            return render(request,'reg.html')
        return render(request, 'reg.html')
        
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something Went Wrong !!!")
        return render(request,'reg.html')


def loginuser(request):
    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            password = request.POST.get('pass')

            user = authenticate(username=uname, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.add_message(request, messages.ERROR, "Invalid credentials!")
                return render(request,'loginpage.html')      
        return render(request,'loginpage.html')
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something Went Wrong !!!")
        return render(request,'loginpage.html')

@login_required(login_url='loginpage')
def home(request):
    if request.user.is_superuser:
        return render(request, 'admin.html')
    elif request.user.is_staff:
        return render(request, 'staff.html')
    elif not request.user.is_superuser and not request.user.is_staff:
        return render(request, 'home.html')
    else:
        return HttpResponse("Admins cannot access this page")

@login_required
def logoutuser(request):
    logout(request)
    return redirect('about')




@login_required
def admin_page(request):
    if request.user.is_superuser:
        return render(request, 'admin.html')
    else:
        return HttpResponse("You are not authorized to access this page")

@login_required
def staff_page(request):
    if request.user.is_staff:
        return render(request, 'staff.html')
    else:
        return HttpResponse("Access Denied")
    
