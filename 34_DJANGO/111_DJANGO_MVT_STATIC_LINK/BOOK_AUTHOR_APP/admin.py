from django.contrib import admin
from BOOK_AUTHOR_APP.models import *

# Register your models here.

class AuthorDisplay(admin.ModelAdmin):
    list_display = ("name", "country")
admin.site.register(Author, AuthorDisplay)

class BookDisplay(admin.ModelAdmin):
    list_display = ("title", "price", "published_year", "author")
admin.site.register(Book, BookDisplay)

