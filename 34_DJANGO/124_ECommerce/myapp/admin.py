from django.contrib import admin
from myapp.models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at',)
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'stock')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')