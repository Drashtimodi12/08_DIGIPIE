from django.contrib import admin
from myapp.models import *

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'phone', 'address', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)    

    def get_user(self, obj):
        return obj.user.username
    get_user.short_description = 'Username'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_category', 'price', 'stock', 'is_active', 'created_at', 'updated_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'stock', 'is_active')

    def get_category(self, obj):
        return obj.category.name
    get_category.short_description = 'Category'




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_product', 'quantity', 'total_price', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('user__username', 'product__name')

    def get_user(self, obj):
        return obj.user.username
    get_user.short_description = 'User'

    def get_product(self, obj):
        return obj.product.name
    get_product.short_description = 'Product'