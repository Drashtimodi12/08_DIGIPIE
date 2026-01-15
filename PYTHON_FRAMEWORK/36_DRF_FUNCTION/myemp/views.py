from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myemp.models import *
from myemp.serializer import *

# Create your views here.

@api_view(['GET'])
def viewemp(request):
    try: 
        allemploye = Employe.objects.all()
        ser = EmployeSerializer(allemploye, many=True)
        return Response({'data':ser.data})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

@api_view(['POST'])
def addemp(request):
    try:
        ser = EmployeSerializer(data=request.data)
        if not ser.is_valid():
            return Response({'errors':ser.errors, 'message':'Something went wrong.'})
        else:
            ser.save()
            return Response({'errors':ser.data, 'message':'Data inserted successfully'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

@api_view(['PUT'])
def updateemp(request, id):
    try:
        employes = Employe.objects.get(pk=id)
        ser =EmployeSerializer(employes, request.data, partial=True)
        if not ser.is_valid():
            return Response({'errors':ser.errors, 'message':'Something went wrong.'})
        else:
            ser.save()
            return Response({'errors': ser.data, 'message': 'Data updated successfully'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})

@api_view(['DELETE'])
def deleteemp(request, id):
    try:
        employes = Employe.objects.get(pk=id)
        employes.delete()
        return Response({'message': 'Student deleted successfully'})
    except Exception as e:
        return Response({'error': str(e), 'message': 'Exception occurred'})