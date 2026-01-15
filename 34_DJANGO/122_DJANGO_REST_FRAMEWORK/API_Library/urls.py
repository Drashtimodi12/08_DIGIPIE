from django.urls import path
from API_Library.views import *

urlpatterns = [
    # ------------------------------------------
    # Author
    # ------------------------------------------
    path('authors', AuthorAPI.as_view()),
    path('authors/<int:id>', AuthorAPIByID.as_view()),
    path('book/author/<int:aid>', BookByAuthorID, name='BookByAuthorID'),


    # ------------------------------------------
    # Publication
    # ------------------------------------------
    path('publication', PublicationAPI.as_view()),
    path('publication/<int:id>', PublicationAPIByID.as_view()),
    path('book/publication/<int:pid>' ,BookByPublicationID, name='BookByPublicationID'),

    # ------------------------------------------
    # Book
    # ------------------------------------------
    path('book', bookview, name='bookview'),
    path('book', bookupdate, name='bookupdate'),
    path('book/author/<int:aid>/publication/<int:pid>', bookadd, name="addbook"),
    path('book/author/<int:aid>/publication/<int:pid>/<int:id>', bookupdate, name="bookupdate"),
    path('book/<int:id>', BookAPIByID.as_view()),


]
