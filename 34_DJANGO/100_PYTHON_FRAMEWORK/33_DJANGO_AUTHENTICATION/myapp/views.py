from django.shortcuts import render, redirect

# Import User model for user management
from django.contrib.auth.models import User

# Import messages for user feedback  link: https://docs.djangoproject.com/en/5.2/ref/contrib/messages/
from django.contrib import messages   

#  Import authentication functions for user login/logout   link: https://docs.djangoproject.com/en/5.2/topics/auth/default/
from django.contrib.auth import authenticate, login, logout

# Import the login_required decorator to protect views that require authentication
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # Check if the user is authenticated
    if request.user.is_anonymous:
        # If the user is not authenticated, render the index page
        return render(request, "index.html")
    else:
        # If the user is authenticated, redirect to the home page
        return redirect("home")
    # return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def adduser(request):
    try:
        if request.method == 'POST':
            data = request.POST
            fname = data.get("fname")
            lname = data.get("lname")
            uname = data.get("uname")
            password = data.get("pass")
            
            # If the username already exists, return an error message
            if User.objects.filter(username=uname).exists():
                messages.add_message(request, messages.ERROR, "Username already exists. Please choose a different one.")
                return render(request, "register.html")
            
            # Create a new user instance and save it to the database
            user = User(first_name=fname, last_name=lname, username=uname)
            user.set_password(password)
            user.save()

            # Optionally, you can use messages to provide feedback
            messages.add_message(request, messages.SUCCESS, "User registered successfully!")
            return render(request, "register.html")
        else:
            return render(request, "register.html")
        
    except Exception as e:
        # If the request method is not POST, return an error message
        messages.add_message(request, messages.ERROR, "Something went wrong. Please try again.")
        return render(request, "register.html", {"error": str(e)})




def loginuser(request):
    try:
        if request.method == 'POST':
            data = request.POST
            uname = data.get("uname")
            password = data.get("pass")

            # Authenticate the user with the provided username and password link: https://docs.djangoproject.com/en/5.2/topics/auth/default/
            user = authenticate(request, username=uname, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                # If authentication is successful, log the user in
                return redirect("home")
            else:
                # If authentication fails, return an error message
                messages.add_message(request, messages.ERROR, "Invalid username or password. Please try again.")
                return render(request, "login.html")

    except Exception as e:
        # If an error occurs, log the error and return an error message
        messages.add_message(request, messages.ERROR, "Something went wrong. Please try again.")
        return render(request, "index.html", {"error": str(e)})

@login_required(login_url="index")   # This decorator ensures that only authenticated users can access this view
def home(request):
    return render(request, "home.html")

@login_required  # This decorator ensures that only authenticated users can access this view
def userlogout(request):
    logout(request)  # Log the user out    
    return render(request, "index.html")



