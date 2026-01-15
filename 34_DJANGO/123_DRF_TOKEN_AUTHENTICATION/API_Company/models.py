from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dep_name
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.emp_name} | {self.salary} | {self.email} | {self.phone} , {self.department.dep_name}"