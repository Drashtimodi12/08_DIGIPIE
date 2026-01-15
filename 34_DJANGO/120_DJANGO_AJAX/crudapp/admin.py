from django.contrib import admin
from crudapp.models import *

# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display = ("username", "email", "age")
admin.site.register(Student, StudentDisplay)