from django.contrib import admin
from Employee_CRUD.models import *

# Register your models here.
class EmployeeDisplay(admin.ModelAdmin):
    list_display = ("name", "department", "age", "phone", "email", "image")
    search_fields = ("name", "department")
    
admin.site.register(Employee, EmployeeDisplay)
