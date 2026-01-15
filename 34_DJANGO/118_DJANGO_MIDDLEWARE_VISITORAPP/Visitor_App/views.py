from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.utils import timezone
from Visitor_App.models import *

# Create your views here.
def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        UserProfile.objects.create(
            username=request.POST['username'],
            age=request.POST['age'],
            email=request.POST['email'],
            contact=request.POST['contact']
        )
        return redirect('/login/')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            user = UserProfile.objects.get(username=username)

            # Create a login activity record
            activite = UserLoginActivity.objects.create(
                user=user,
                login_time = timezone.now()
            )
            # Pass username as string in URL
            # Redirect to home page after login and include activity id so logout can update it
            return redirect(f'/home/?username={user.username}&activity_id={activite.id}')
        except UserProfile.DoesNotExist:
            # If user is not found, show message
            messages.error(request, "User not found, please signup first")
            return redirect('login')  # Redirect back to login page
    return render(request, 'login.html')

def home(request):
    username = request.GET.get('username')
    activity = None
    activity_id = request.GET.get('activity_id')
    if activity_id:
        try:
            activity = UserLoginActivity.objects.get(id=activity_id)
        except UserLoginActivity.DoesNotExist:
            activity = None
    if username:
        # include total signup count
        signup_count = UserProfile.objects.count()
        return render(request, 'home.html', {'user': username, 'activity': activity, 'signup_count': signup_count})
    else:
        return redirect('login')
    
    
def logout(request):
    username = request.GET.get('user')
    activity_id  = request.GET.get('activity_id')

    if activity_id:
        try:
            activity = UserLoginActivity.objects.get(id=activity_id)
            activity.logout_time = timezone.now()
            # Calculate total time in seconds
            activity.total_seconds = int((activity.logout_time - activity.login_time).total_seconds())
            activity.save()
        except UserLoginActivity.DoesNotExist:
            pass

    return render(request, 'logout.html', {'user' : username})