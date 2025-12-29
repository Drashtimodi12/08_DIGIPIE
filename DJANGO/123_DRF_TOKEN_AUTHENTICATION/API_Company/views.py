from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from API_Company.models import *
from API_Company.serializer import *

# Create your views here.

# ---------- Department ----------
class departmentAPI(APIView):

    # ------------------------
    # Authentication
    # ------------------------
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            alldep = Department.objects.all()
            ser = DepartmentSerializer(alldep, many=True)
            return Response({"department":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})
        
    def post(delf, request):
        try:
            ser = DepartmentSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"department":ser.data,"message":"Department added successfully!"})
            return Response({"errors":ser.errors, "message":"Something wents Wrong!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

class departmentAPIByID(APIView):
    def get(self, request, id):
        try:
            department = Department.objects.get(pk=id)
            ser = DepartmentSerializer(department)
            return Response({"department":ser.data}) 
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

    def patch(self, request, id):
        try:
            department = Department.objects.get(pk=id)
            ser = DepartmentSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"department":ser.data})
            return Response({"error":ser.errors, "message":"Something wents Wrong!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})


    def delete(self, request, id):
        try:
            department = Department.objects.get(pk=id)
            department.delete()
            return Response({"department":"Deleted successfully!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})

        

# ---------- Employee ----------
@api_view(['GET'])
def employeeview(request):
    try:
        allemp = Employee.objects.all()
        ser = EmployeeSerializer(allemp, many=True)
        return Response({"employee":ser.data})
    except Exception as e:
        return Response({"errors":str(e), "message":"Something wents Wrong!"})
        
@api_view(['POST'])        
def employeeadd(request, did):
    try:
        dep = Department.objects.get(pk=did)
        data=request.data
        data['department'] = dep.id
        ser = EmployeeSerializer(data=data)
        if ser.is_valid():
            ser.save(department=dep)
            return Response({"employee":ser.data, "message":"Employee added successfully!"})
        return Response({"errors":ser.errors, "message":"Something wents Wrong!"})
    except Exception as e:
        return Response({"errors":str(e), "message":"Something wents Wrong!"})

@api_view(['PATCH'])
def employeeupdate(request, did, id):
    try:
        department = Department.objects.get(pk=did)
        emp = Employee.objects.get(pk=id)
        data = request.data
        data['department'] = department.id
        ser = EmployeeSerializer(emp, data=data, partial=True)
        if ser.is_valid():
            ser.save( department=department)
            return Response({"employee":ser.data, "message":"Employee updated successfully!"})
        return Response({"error":ser.errors, "message":"Something wents Wrong!"})
    except Exception as e:
        return Response({"errors":str(e), "message":"Something wents Wrong!"})

class EmployeeAPIByID(APIView):
    def get(self, request, id):
        try:
            emp = Employee.objects.get(pk=id)
            ser = EmployeeSerializer(emp)
            return Response({"employee":ser.data})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})
                
    def delete(self, request, id):
        try:
            emp = Employee.objects.get(pk=id)
            emp.delete()
            return Response({"employee":"Deleted successfully!"})
        except Exception as e:
            return Response({"errors":str(e), "message":"Something wents Wrong!"})