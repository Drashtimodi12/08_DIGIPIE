from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mystu.models import *
from mystu.serializer import *

# Create your views here.

@api_view(['GET'])
def viewstu(request):
    allstudents = Student.objects.all()
    ser = StudentSerializer(allstudents, many=True)
    return Response({'Students':ser.data})

@api_view(['POST'])
def addstu(request):
    try:
        ser = StudentSerializer(data=request.data)
        if not ser.is_valid():
            return Response({'errors':ser.errors, 'message':'Something went wrong.'})
        else:
            ser.save()
            return Response({'data':ser.data, 'message':'Data inserted successfully'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

@api_view(['PUT'])
def updatestu(request, id):
    try:
        students = Student.objects.get(pk=id)
        # ser = StudentSerializer(students, request.data)     # Replace all fields
        ser = StudentSerializer(students, request.data, partial=True)       # Update only given fields. Work as a PATCH request.
        if not ser.is_valid():
            return Response({'errors':ser.errors, 'message':'Something went wrong.'})
        else:
            ser.save()
            return Response({'data':ser.data, 'message':'Data updated successfully'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

@api_view(['DELETE'])
def deletestu(request, id):
    try:
        students = Student.objects.get(pk=id)
        students.delete()
        return Response({'message': 'Student deleted successfully'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

