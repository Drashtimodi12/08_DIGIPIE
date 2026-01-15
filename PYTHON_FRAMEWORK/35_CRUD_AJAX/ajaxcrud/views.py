from django.shortcuts import render
from django.http import HttpResponse
from ajaxcrud.models import *
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html') 


def addstu(request):
    if request.method == 'POST':
        data = request.POST
        # print(data)
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')

        Student.objects.create(name=name, email=email, age=age)
        return HttpResponse("Student added successfully!")

def fetchStudents(request):
    alldata = Student.objects.all()
    return JsonResponse({"data": list(alldata.values())})

def deletedata(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    student.delete()
    return HttpResponse("Data deleted successfully!")


def databyid(request):
    sid = request.GET['sid']
    students = Student.objects.filter(id=sid)
    return JsonResponse({"data": list(students.values())})

def updatedata(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')

        students = Student.objects.get(pk=id)
        students.name = data.get('name')
        students.email = data.get('email')
        students.age = data.get('age')

        students.save()
        return HttpResponse("Data updated successfully!")
    
def searchdata(request):
    keyword = request.GET['value']
    filterdata = Student.objects.filter(name__startswith=keyword)
    return JsonResponse({"data": list(filterdata.values())})