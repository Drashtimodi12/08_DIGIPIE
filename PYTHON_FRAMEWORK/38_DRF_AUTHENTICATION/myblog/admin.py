from django.contrib import admin
from myblog.models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'created_at']
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'commenter', 'comment_text', 'created_at']
admin.site.register(Comment, CommentAdmin)