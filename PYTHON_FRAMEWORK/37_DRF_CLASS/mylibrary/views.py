from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from mylibrary.models import *
from mylibrary.serializers import *

# Create your views here.

class AuthorAPI(APIView):
    def get(self, request):
        try:
            allauthor = Author.objects.all()
            ser = AuthorSerializer(allauthor, many=True)
            return Response({'data':ser.data})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})
        
    def post(self, request):
        try:
            ser = AuthorSerializer(data=request.data)
            if not ser.is_valid():
                return Response({'errors':ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'data': ser.data, 'message': 'Author inserted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

class AuthorAPIByID(APIView):
    def get(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            ser = AuthorSerializer(author)
            return Response({'data':ser.data})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

    def patch(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            ser = AuthorSerializer(author, request.data, partial=True)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'data': ser.data, 'message': 'Author updated successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

    def delete(self, request, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
            return Response({'message': 'Author deleted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})










class PublicationAPI(APIView):
    def get(self, request):
        try:
            allpublication = Publication.objects.all()
            ser = PublicationSerializer(allpublication, many=True)
            return Response({'data':ser.data})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})
        
    def post(self, request):
        try:
            ser = PublicationSerializer(data=request.data)
            if not ser.is_valid():
                return Response({'errors':ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'data': ser.data, 'message': 'Publication inserted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

class PublicationAPIByID(APIView):

    def get(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            ser = PublicationSerializer(publication)
            return Response({'data':ser.data})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

    def patch(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            ser = PublicationSerializer(publication, request.data, partial=True)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'data': ser.data, 'message': 'Publication updated successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

    def delete(self, request, id):
        try:
            publication = Publication.objects.get(pk=id)
            publication.delete()
            return Response({'message': 'Publication deleted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})










@api_view(['GET'])
def BookList(request):
    try:
        allbook = Book.objects.all()
        ser = BookSerializer(allbook, many=True)
        return Response({'data': ser.data})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})
    
@api_view(['POST'])
def BookAdd(request, aid, pid):
    try:
        author = Author.objects.get(pk=aid)  # Corrected
        publication = Publication.objects.get(pk=pid)  # Corrected
        data = request.data
        data['author'] = author.id
        data['publication'] = publication.id
        ser = BookSerializer(data=data)
        if not ser.is_valid():
            return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
        else:
            ser.save()
            return Response({'data': ser.data, 'message': 'Book inserted successfully.'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

@api_view(['PUT'])
def BookUpdate(request, aid, pid, id):
    try:
        author = Author.objects.get(pk=aid)
        publication = Publication.objects.get(pk=pid)
        book = Book.objects.get(pk=id)
        data = request.data
        data['author'] = author.id
        data['publication'] = publication.id
        ser = BookSerializer(book, data=data, partial=True)
        if not ser.is_valid():
            return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
        else:
            ser.save()
            return Response({'data': ser.data, 'message': 'Book updated successfully.'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

class BookAPIByID(APIView):

    def get(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            ser = BookSerializer(book)
            return Response({'data':ser.data})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})

    def delete(self, request, id):
        try:
            book = Book.objects.get(pk=id)
            book.delete()
            return Response({'message': 'Book deleted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})        
    









@api_view(['GET'])
def BookByAuthor(request, aid):
    try:
        author = Author.objects.get(pk=aid)
        book = Book.objects.filter(author=author)
        ser = BookSerializer(book, many=True)
        return Response({'data':ser.data})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})
    









@api_view(['GET'])
def BookByPublication(request, pid):
    try:
        publication = Publication.objects.get(pk=pid)
        book = Book.objects.filter(publication=publication)
        ser = BookSerializer(book, many=True)
        return Response({'data':ser.data})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})