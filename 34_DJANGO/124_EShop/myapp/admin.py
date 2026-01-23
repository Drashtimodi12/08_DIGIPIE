from django.contrib import admin
from myapp.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'category')
admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'created_at')
admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
admin.site.register(OrderItem, OrderItemAdmin)
