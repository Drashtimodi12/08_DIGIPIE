from django.contrib import admin
from mylibrary.models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Author, AuthorAdmin)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Publication, PublicationAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'qty', 'author', 'publication']
admin.site.register(Book, BookAdmin)