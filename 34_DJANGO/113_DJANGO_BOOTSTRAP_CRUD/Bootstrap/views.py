from django.shortcuts import render, redirect
import os
from Bootstrap.models import *

# Create your views here.

def form(request):
    allStudents = Student.objects.all()
    return render(request, 'form.html', {'students':allStudents})

def register(request):
    if request.method == 'POST':
        id = request.POST['id']
        username=request.POST['uname']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        image = request.FILES.get('img') if request.FILES else None

        if id:
            stud = Student.objects.get(pk=id)
            # os.remove(stud.image.path)
            stud.username=username
            stud.email=email
            stud.phone=phone
            stud.age=age
            if image:
                try:
                    if stud.image and stud.image.path and os.path.exists(stud.image.path):
                        os.remove(stud.image.path)
                except Exception:
                    pass
                stud.image = image
            stud.save()

        else:
            Student.objects.create(
                username=username,
                email=email,
                phone=phone,
                age=age,
                image=image
            )
        return redirect('form')    
    return redirect('form')


def delete(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    try:
        if student.image and student.image.path and os.path.exists(student.image.path):
            os.remove(student.image.path)
    except Exception:
        pass
    student.delete()
    return redirect("form")
   

def edit(request):
    sid = request.GET['sid']
    student = Student.objects.get(pk=sid)
    allStudents = Student.objects.all()
    return render(request,"form.html",{"students":allStudents,"student":student})