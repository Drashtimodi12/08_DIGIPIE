from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from myapp.models import *
from myapp.serializers import *

# Create your views here.

class ProductAPI(APIView):
    def get(self, request):
        # return Response({'message': 'GET API Calling.'})
        try:
            allproducts = Product.objects.all()
            ser = ProductSerializer(allproducts, many=True)
            return Response({'data':ser.data})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})
    
    def post(self, request):
        # return Response({'message': 'POST API Calling.'})
        try:
            ser = ProductSerializer(data = request.data)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'data': ser.data, 'message': 'Data inserted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})
    
    def put(self, request):
        # return Response({'message': 'PUT API Calling.'})
        try:
            products = Product.objects.get(pk=request.data.get('id'))
            if not products:
                return Response({'message':'Product Not Found'})
            ser = ProductSerializer(products, request.data)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'data': ser.data, 'message': 'Data updated successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})
    
    def delete(self, request):
        # return Response({'message': 'DELETE API Calling.'})
        try:
            products = Product.objects.get(pk=request.data.get('id'))
            if not products:
                return Response({'message':'Product Not Found'})
            else:
                products.delete()
                return Response({'message': 'Product deleted successfully.'})
        except Exception as e:
            return Response({'error': str(e), 'message': 'Exception occurred'})