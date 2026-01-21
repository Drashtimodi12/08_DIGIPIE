from django.shortcuts import render, redirect
from myapp.models import *
import os

# Create your views here.

def index(request):
    allStudents = Student.objects.all()
    return render(request, 'index.html', {"students": allStudents})

def register(request):
    if request.method=='POST':
        id=request.POST['id']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        image=""
        if request.FILES:
            image=request.FILES['img']

        if(id):
            # print(image)
            stud=Student.objects.get(pk=id)
            stud.name=name
            stud.email=email
            stud.phone=phone
            stud.age=age

            if image:
                os.remove(stud.image.path)
                stud.image=image
            stud.save()
        else:
            Student.objects.create(name=name, email=email, phone=phone, age=age, image=image)
        # return render(request, "index.html", {"message":"Student Register Succesfully"})
        return redirect('index')
            
    # return render(request, "index.html")
    # return redirect(request, 'index')
    return redirect('index')


def edit(request):
    sid = request.GET.get('sid')
    try:
        student = Student.objects.get(pk=sid)
        allStudents = Student.objects.all()
        return render(request, 'index.html', {"students": allStudents, 'student': student})
    except Student.DoesNotExist:
        return redirect('index')
      

def delete(request):
    stid = request.GET.get('sid')
    if stid:
        try:
            student = Student.objects.get(pk=stid)
            os.remove(student.image.path)
            student.delete()
        except Student.DoesNotExist:
            return render(request, 'index.html', {'error': 'Student not found.'})
        return redirect('index')