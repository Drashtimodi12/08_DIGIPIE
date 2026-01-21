from django.contrib import admin
from myemp.models import *

# Register your models here.

class EmployeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'salary', 'department']
admin.site.register(Employe, EmployeAdmin)