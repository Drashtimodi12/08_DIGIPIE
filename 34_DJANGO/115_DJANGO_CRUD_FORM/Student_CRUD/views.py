from django.shortcuts import render, redirect
from django.http import HttpResponse
from Student_CRUD.models import *

# Create your views here.

def index(request):
    allStudent = Student.objects.all()
    return render(request, 'index.html', {"stu" : allStudent})

def register(request):
    if request.method=='POST':
        data = request.POST
        # print(data)
        id = data.get('id')
        username = data.get('uname')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')

        if id:
            stu = Student.objects.get(pk=id)
            stu.username=username
            stu.email=email
            stu.phone=phone
            stu.age=age
            stu.save()
        else:
            Student.objects.create(
                username = username,
                email=email,
                phone=phone,
                age=age
            )
            # return render(request, 'index.html', {"msg" : "Registration Successfully!"})
            return redirect('index')
    return redirect('index')


def update(request):
    stuid = request.GET.get('stuid')
    stu = Student.objects.get(pk=stuid)
    allStudent = Student.objects.all()
    return render(request, 'index.html', {"ustu" : stu, "stu" : allStudent})




def delete(request):
    stuid = request.GET.get('stuid')
    stu = Student.objects.get(pk=stuid)
    stu.delete()
    return redirect('index')