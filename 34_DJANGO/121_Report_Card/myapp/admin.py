from django.contrib import admin
from myapp.models import *

# Register your models here.

# we use for specifying data to be displayed in admin panel
class DepartmentData(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Department, DepartmentData)


    
admin.site.register(StudentID)



class StudentData(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'dept', 'stid']

admin.site.register(Student, StudentData)



class SubjectData(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Subject)



class MarksData(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
    
admin.site.register(Marks, MarksData)
