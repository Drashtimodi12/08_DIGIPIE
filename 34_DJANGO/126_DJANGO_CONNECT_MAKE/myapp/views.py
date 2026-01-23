from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import *
import requests     # To send HTTP requests to Make.com


# -----------------------------
# Make.com Webhook URL
# -----------------------------
# This is the URL of your Make.com custom webhook
MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/1v7ai3zqv6o63dkqemddmsivaa6cjjvj"


# -----------------------------
# Index View
# ----------------------------- 
def index(request):
    allStudent = Student.objects.all()      # Fetch all students from DB
    return render(request, 'index.html', {"stu" : allStudent})


# -----------------------------
# Register View
# -----------------------------
def register(request):
    if request.method=='POST':
        data = request.POST
        # print(data)
        id = data.get('id')
        username = data.get('uname')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')

        # UPDATE existing student
        if id:
            stu = Student.objects.get(pk=id)
            stu.username=username
            stu.email=email
            stu.phone=phone
            stu.age=age
            stu.save()

            # 🔔 Send "student_updated" event to Make.com
            payload = {
                "event": "student_updated",
                "id": stu.id,
                "name": stu.username,
                "email": stu.email,
                "phone": stu.phone,
                "age": stu.age
            }
            # requests.post()(Send a POST HTTP request); MAKE_WEBHOOK_URL(Server URL where data is sent); json=payload(Convert Python dict to JSON and send it)
            requests.post(MAKE_WEBHOOK_URL, json=payload)       
        else:
            # CREATE new student
            stu = Student.objects.create(
                username = username,
                email=email,
                phone=phone,
                age=age
            )

            # 🔔 Send "student_created" event to Make.com
            payload = {
                "event": "student_created",
                "id": stu.id,
                "name": stu.username,
                "email": stu.email,
                "phone": stu.phone,
                "age": stu.age
            }
            requests.post(MAKE_WEBHOOK_URL, json=payload)
            # return render(request, 'index.html', {"msg" : "Registration Successfully!"})

        return redirect('index')        # Redirect back to index after save
    return redirect('index')    # If not POST, redirect to index



# -----------------------------
# Update View
# -----------------------------
def update(request):
    stuid = request.GET.get('stuid')  # Get student ID from query param
    stu = Student.objects.get(pk=stuid)  # Fetch student object
    allStudent = Student.objects.all()  # Fetch all students
    return render(request, 'index.html', {"ustu": stu, "stu": allStudent})


# -----------------------------
# Delete View
# -----------------------------
def delete(request):
    stuid = request.GET.get('stuid')  # Get student ID from query param
    stu = Student.objects.get(pk=stuid)  # Fetch student object

    # 🔔 Send "student_deleted" event to Make.com
    payload = {
        "event": "student_deleted",
        "id": stu.id,
        "name": stu.username,
        "email": stu.email,
        "phone": stu.phone,
        "age": stu.age
    }
    requests.post(MAKE_WEBHOOK_URL, json=payload)

    stu.delete()
    return redirect('index')
