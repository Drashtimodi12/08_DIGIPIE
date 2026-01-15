from django.db import models

# Create your models here.
# ------------------------
# Student
# ------------------------
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    age = models.IntegerField()

# ------------------------
# Employee
# ------------------------
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    salary = models.FloatField()


# ------------------------
# Product
# ------------------------
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()