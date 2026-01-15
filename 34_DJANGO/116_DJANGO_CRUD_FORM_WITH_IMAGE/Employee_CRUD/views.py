from django.shortcuts import render, redirect
from Employee_CRUD.models import *
import os
# Create your views here.


def form(request):
    allemp = Employee.objects.all()
    return render(request, 'form.html', {'emp' : allemp})


def registerEmp(request):
    if request.method == 'POST':
        data = request.POST
        # print(data)
        emp_id = data.get('id')
        name = data.get('name')
        department = data.get('department')
        age = data.get('age')
        phone = data.get('phone')
        email = data.get('email')
        image = request.FILES.get('file')

        if emp_id:
            emp = Employee.objects.get(pk=emp_id)
            emp.name = name
            emp.department = department
            emp.age = age
            emp.phone = phone
            emp.email = email

            # update image only if a new file was uploaded
            if image:
                if emp.image and os.path.isfile(emp.image.path):
                    os.remove(emp.image.path)
                emp.image = image
            else:     
                emp.save()
                return redirect('form')
            
        else:
            # create with uploaded image if present
            Employee.objects.create(
                name=name,
                department=department,
                age=age,
                phone=phone,
                email=email,
                image=image
            )
            
    return redirect('form')

def updateEmp(request):
    empid = request.GET.get('empid')        # /updateEmp?empid=3
    employee = Employee.objects.get(pk=empid)       # Fetches one Employee object from the database
    allemp = Employee.objects.all()     # Retrieves all employee records
    return render(request, 'form.html', {'uemp' : employee, 'emp' : allemp})

def deleteEmp(request):
    empid = request.GET.get('empid')
    employee = Employee.objects.get(pk=empid)
    
    # remove image file if it exists
    if employee.image and os.path.isfile(employee.image.path):
        os.remove(employee.image.path)
    employee.delete()
    return redirect('form')