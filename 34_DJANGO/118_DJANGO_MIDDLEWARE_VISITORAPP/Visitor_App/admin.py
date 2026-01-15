from django.contrib import admin
from Visitor_App.models import *

# Register your models here.

class UserProfileDisplay(admin.ModelAdmin):
    list_display = ("username", "age", "email", "contact", "created_at")
admin.site.register(UserProfile, UserProfileDisplay)

class UserLoginActivityDisplay(admin.ModelAdmin):
    list_display = ("user", "login_time", "logout_time", "total_seconds")

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'User'

admin.site.register(UserLoginActivity, UserLoginActivityDisplay)