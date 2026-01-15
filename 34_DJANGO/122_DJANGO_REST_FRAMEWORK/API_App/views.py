from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView

from API_App.models import *
from API_App.serializer import *

# Create your views here.


# ----------------------------------------------------------
# Student
# ----------------------------------------------------------
@api_view(['GET'])
def view(request):
    allStu = Student.objects.all()
    ser = StudentSerializer(allStu, many = True)
    return Response({"students":ser.data})
    # return Response({"message":"Get api calling..."})

@api_view(['POST'])
def add(request):
    # print(request.data)
    # return Response({"message":"POST API calling..."})
    try:
        ser = StudentSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"Data inserted successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})

@api_view(['PUT'])
def update(request, id):
    # return Response({"message":"PUT API calling..."})
    try:
        stu = Student.objects.get(pk=id)
        ser = StudentSerializer(stu, request.data, partial=True)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"Data updated successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})

@api_view(['DELETE'])
def delete(request, id):
    # return Response({"message":"DELETE API calling..."})
    try:
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"success":True})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})


# ----------------------------------------------------------
# Employee
# ----------------------------------------------------------
@api_view(['GET'])
def view_emp(request):
    try: 
        allEmp = Employee.objects.all()
        ser = EmployeeSerialzer(allEmp, many = True)
        return Response({"employee":ser.data})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})
    
@api_view(['POST'])
def add_emp(request):
    try:
        ser = EmployeeSerialzer(data=request.data)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message": "Data inserted successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})


@api_view(['PUT'])
def update_emp(request, id):
    try:
        emp = Employee.objects.get(pk=id)
        ser = EmployeeSerialzer(emp, request.data, partial=True)
        if not ser.is_valid():
            return Response({"errors": ser.errors, "message":"Something went wrong..."})
        else:
            ser.save()
            return Response({"data":ser.data, "message":"Data updated successfully..."})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})

@api_view(['DELETE'])
def delete_emp(request,id):
    try:
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({"Success":True})
    except Exception as e:
        return Response({"error":e, "message":"Something went wrong..."})



# ----------------------------------------------------------
# Product
# ----------------------------------------------------------
class ProductAPI(APIView):
    def get(self, request):
        # return Response({"message":"GET api calling..."})
        try:
            allProduct = Product.objects.all()
            ser = ProductSerializer(allProduct, many=True)
            return Response({"product":ser.data})
        except Exception as e:
            return Response({"error":e, "message":"Something went wrong..."})
    

    def post(self, request):
        # return Response({"message":"POST api calling..."})
        try:
            ser = ProductSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"errors": ser.errors, "message":"Something went wrong..."})
            else:
                ser.save()
                return Response({"data": ser.data, "message":"Products add successfully..."})
        except Exception as e:
            return Response({"error":e, "message":"Something went wrong..."})


    def put(self, request): 
        # return Response({"message":"PUT api calling..."})
        try:
            product = Product.objects.get(pk=request.data.get('id'))
            if not product:
                return Response({"message":"Product not found"})
            else:
                ser = ProductSerializer(product, request.data, partial=True)
            if not ser.is_valid():
                return Response({"error":ser.errors, "message":"Something went wrong..."})
            else:
                ser.save()
                return Response({"date":ser.data})
        except Exception as e:
            return Response({"error":e, "message":"Something went wrong..."})


    def delete(self, request):
        # return Response({"message":"DELETE api calling..."})
        try:
            product = Product.objects.get(pk=request.data.get('id'))
            if not product:
                return Response({"message":"Product not found"})
            else:
                product.delete()
                return Response({"sucess":True})
        except Exception as e:
            return Response({"error":e, "message":"Something went wrong..."})
