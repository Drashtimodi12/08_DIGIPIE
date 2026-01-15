from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from crudapp.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_data(request):
    if request.method=='POST':
        data = request.POST
        # print(data)
        uname = data.get("uname")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(username=uname,email=email,age=age)
        return HttpResponse("Registration successfully !!!")
    
def loaddata(request):
    alldata = Student.objects.all()
    return JsonResponse({'data':list(alldata.values())})


def deletedata(request):
    sid = request.GET['sid']
    students = Student.objects.get(pk=sid)
    students.delete()
    return HttpResponse("Student Deleted Successfully!")

def databyid(request):
    sid = request.GET['sid']
    student = Student.objects.filter(id=sid)
    return JsonResponse({"data":list(student.values())})

def updatedata(request):
    if request.method=='POST':
        data = request.POST
        # print(data)
        id = data.get("id")
        stu = Student.objects.get(pk=id)
        stu.username = data.get("uname")
        stu.email = data.get("email")
        stu.age = data.get("age")

        stu.save()

        return HttpResponse("Updated Successfully!!")
    

def searchdata(request):
    keyword = request.GET.get('value')
    filteredData = Student.objects.filter(username__startswith=keyword)
    return JsonResponse({"data":list(filteredData.values())})