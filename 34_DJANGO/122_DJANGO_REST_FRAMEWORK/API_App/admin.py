from django.contrib import admin
from API_App.models import *

# Register your models here.

# ------------------------
# Student
# ------------------------
class StudentDisplay(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "age")
admin.site.register(Student, StudentDisplay)


# ------------------------
# Employee
# ------------------------
class EmployeeDisplay(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "department", "salary")
admin.site.register(Employee, EmployeeDisplay)


# ------------------------
# Product
# ------------------------
class ProductDisplay(admin.ModelAdmin):
    list_display = ("name", "price", "description", "stock")
admin.site.register(Product, ProductDisplay)
