from django.contrib import admin
from API_Company.models import *

# Register your models here.

class DepartmentDisplay(admin.ModelAdmin):
    list_display = ("dep_name",)
admin.site.register(Department, DepartmentDisplay)

class EmployeeDisplay(admin.ModelAdmin):
    list_display = ("emp_name", "salary", "email", "phone", "department")
admin.site.register(Employee, EmployeeDisplay)