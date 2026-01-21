from django.contrib import admin
from django.urls import path, include
from mylibrary.views import *

urlpatterns = [
    path('author', AuthorAPI.as_view()),
    path('author/<int:id>', AuthorAPIByID.as_view()),

    path('publication', PublicationAPI.as_view()),
    path('publication/<int:id>', PublicationAPIByID.as_view()),

    path('book', BookList, name='BookList'),
    path('book/author/<int:aid>/publication/<int:pid>', BookAdd, name='BookAdd'),

    path('book/<int:id>', BookAPIByID.as_view()),

    path('book/author/<int:aid>/publication/<int:pid>/<int:id>', BookUpdate, name='BookUpdate'),

    path('book/author/<int:aid>', BookByAuthor, name='BookByAuthor'),
    path('book/publication/<int:pid>', BookByPublication, name='BookByPublication'),
]
