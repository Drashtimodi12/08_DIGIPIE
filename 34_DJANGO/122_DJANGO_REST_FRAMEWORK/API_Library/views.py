from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from API_Library.models import *
from API_Library.serializer import *

# Create your views here.

# ------------------------------------------
# Author
# ------------------------------------------
class AuthorAPI(APIView):
    def get(self, request):
        try:
            allauthor = Author.objects.all()
            ser = AuthorSerializer(allauthor, many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    def post(self, request):
        try:
            ser = AuthorSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"data":ser.data, "message":"Author add successfully!"})
            return Response({"errors":ser.errors, "message":"Something wents Wrong!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})


class AuthorAPIByID(APIView):
    def get(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            ser = AuthorSerializer(author)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})


    def put(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            ser = AuthorSerializer(author, request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"data":ser.data, "message":"Author updated successfully!"})
            return Response({"errors":ser.errors, "message":"Validation failed!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    def delete(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
            return Response({"success":True})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

@api_view(['GET'])
def BookByAuthorID(request, aid):
    try:
        author = Author.objects.get(pk=aid)
        books = Book.objects.filter(author=author)
        ser = BookSerializer(books, many = True)
        return Response({"data":ser.data})
    except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})
    






# ------------------------------------------
# Publication
# ------------------------------------------
class PublicationAPI(APIView):
    def get(self, request):
        try:
            allpublications = Publication.objects.all()
            ser = PublicationSerializer(allpublications, many=True)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})
        
    def post(self, request):
        try:
            ser = PublicationSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"data":ser.data, "message":"Publication add successfully!"})
            return Response({"errors":ser.errors, "message":"Something wents Wrong!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

class PublicationAPIByID(APIView):
    def get(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            ser = PublicationSerializer(publication)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    def patch(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            ser = PublicationSerializer(publication, request.data)
            if ser.is_valid():
                ser.save()
                return Response({"data":ser.data, "message":"Author updated successfully!"})
            return Response({"errors":ser.errors, "message":"Validation failed!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    def delete(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            publication.delete()
            return Response({"success":True})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

@api_view(['GET'])    
def BookByPublicationID(request, pid):
    try:
        publications = Publication.objects.get(pk=pid)
        books = Book.objects.filter(publication=publications)
        ser = BookSerializer(books, many = True)
        return Response({"data":ser.data})
    except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})





# ------------------------------------------
# Book
# ------------------------------------------
@api_view(['GET'])
def bookview(request):
    try:
        allbook = Book.objects.all()
        ser = BookSerializer(allbook, many=True)
        return Response({"data":ser.data})
    except Exception as e:
        return Response({"errors":str(e), "message":"Something wents Wrong!"})

@api_view(['POST'])
def bookadd(request, aid, pid):
    try:
        # Get related objects
        author = Author.objects.get(pk=aid)
        publication = Publication.objects.get(pk=pid)
        data = request.data
        data['author'] = author.id
        data['publication'] = publication.id
        # Pass request data to serializer 
        ser = BookSerializer(data=data)
        if ser.is_valid():
             # Save book with foreign key relations
            ser.save(author=author, publication=publication)
            return Response({"data":ser.data, "message":"Book add successfully!"})
        return Response({"errors":ser.errors, "message":"Validation failed!"})
    except Exception as e:
        return Response({"errors":str(e), "message":"Something wents Wrong!"})

@api_view(['PATCH'])
def bookupdate(request, aid, pid, id):           
    try:
        author = Author.objects.get(pk=aid)
        publication = Publication.objects.get(pk=pid)
        book = Book.objects.get(pk=id)
        data = request.data
        data['author'] = author.id
        data['publication'] = publication.id
        ser = BookSerializer(book, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"data":ser.data, "message":"Book updated successfully!"})
    except Exception as e:
        return Response({"errors":str(e), "message":"Something wents Wrong!"})




class BookAPIByID(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id) 
            ser = BookSerializer(book)
            return Response({"data":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    def delete(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return Response({"success":True})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    



