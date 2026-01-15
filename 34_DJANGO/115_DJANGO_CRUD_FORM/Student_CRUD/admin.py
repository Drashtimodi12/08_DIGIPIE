from django.contrib import admin
from Student_CRUD.models import *

# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display = ("username", "email", "phone", "age")
admin.site.register(Student, StudentDisplay)