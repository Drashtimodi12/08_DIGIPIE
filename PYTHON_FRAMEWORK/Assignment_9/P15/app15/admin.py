from django.contrib import admin
from app15.models import *

# Register your models here.

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Specialty, SpecialtyAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'phone', 'experience_years')
admin.site.register(Doctor, DoctorAdmin)