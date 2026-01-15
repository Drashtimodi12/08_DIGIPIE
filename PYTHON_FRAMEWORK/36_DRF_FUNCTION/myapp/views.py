from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'message': 'GET API Calling'})

@api_view(['POST'])
def add(request):
    return Response({'message': 'POST API Calling'})

@api_view(['PUT'])
def update(request):
    return Response({'message': 'PUT API Calling'})

@api_view(['DELETE'])
def delete(request):
    return Response({'message': 'DELETE API Calling'})