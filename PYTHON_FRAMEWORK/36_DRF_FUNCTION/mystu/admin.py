from django.contrib import admin
from mystu.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'age']
admin.site.register(Student, StudentAdmin)