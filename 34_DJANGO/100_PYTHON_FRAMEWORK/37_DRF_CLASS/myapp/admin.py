from django.contrib import admin
from myapp.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'stock']
admin.site.register(Product, ProductAdmin)