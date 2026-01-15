from django.contrib import admin
from API_Library.models import *

# Register your models here.

# ------------------------------------------
# Author
# ------------------------------------------
class AuthorDisplay(admin.ModelAdmin):
    list_display = ("Author_Name",)
admin.site.register(Author, AuthorDisplay)


# ------------------------------------------
# Publication
# ------------------------------------------
class PublicationDisplay(admin.ModelAdmin):
    list_display = ("Publication_Name",)
admin.site.register(Publication, PublicationDisplay)


# ------------------------------------------
# Book
# ------------------------------------------
class BookDisplay(admin.ModelAdmin):
    list_display = ("title", "price", "author", "publication")
admin.site.register(Book, BookDisplay)
