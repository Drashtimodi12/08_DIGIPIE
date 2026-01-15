from django.db import models


# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.username} | {self.email} | {self.phone} | {self.age}"
    

class Employee(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return f"{self.name} | {self.department} | {self.email} | {self.phone} | {self.age}"
    