# ==============================
# Django shortcut functions
# ==============================
from django.shortcuts import render, redirect
# render   → return HTML template with context
# redirect → redirect user to another URL

# ==============================
# Django HTTP Responses
# ==============================
from django.http import HttpResponse, JsonResponse
# HttpResponse → return simple text / HTML response
# JsonResponse → return JSON response (mostly for AJAX / APIs)

# ==============================
# Django Authentication System
# ==============================
from django.contrib.auth.models import User     # Default Django User model: represents users in the database
from django.contrib.auth import authenticate, login, logout
# authenticate → validate username & password
# login        → create user session
# logout       → destroy user session

from django.contrib.auth.decorators import login_required       # login_required → restrict view access to logged-in users only
from django.contrib import messages     # messages → display success/error messages in templates onetime
 
# ==============================
# Django REST Framework (DRF)
# ==============================
from rest_framework.response import Response    # Response → return API responses in JSON format
from rest_framework.decorators import api_view      # api_view → function-based API views (@api_view(['GET', 'POST']))
from rest_framework.views import APIView            # APIView → class-based API views  (class MyView(APIView))

# ==============================
# DRF Authentication & Permissions
# ==============================
from rest_framework.authentication import (
    BasicAuthentication,            # BasicAuthentication   → username & password in headers
    SessionAuthentication           # SessionAuthentication → browser-based login session
)
from rest_framework.permissions import (
    IsAuthenticated,        # IsAuthenticated → only logged-in users can access API
    AllowAny                # AllowAny        → anyone can access API

)

# ==============================
# JWT Authentication (SimpleJWT)
# ==============================
from rest_framework_simplejwt.authentication import JWTAuthentication       # JWTAuthentication → token-based authentication using JWT

# ==============================
# Project-specific imports
# ==============================
from myapp.models import *      # Import database all models
from myapp.serializers import *     # Import serializers for converting model data to JSON

# Create your views here


# ==============================
# User APIs
# ==============================
@api_view(['GET'])
def get_users(request):
    try:
        alluser = User.objects.all()
        # ser = UserSerializer(alluser, many=True)
        # return Response({'user': ser.data})
        return render(request, 'userprofile.html', {'user': alluser})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'})


@api_view(['GET'])
def get_usersbyId(request, id):
    try:
        user = User.objects.get(pk=id)
        ser = UserSerializer(user)
        return Response({'user': ser.data})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'})


# ==============================
# UserProfile APIs
# ==============================
@api_view(['GET'])
def get_userprofile(request):
    try:
        alluser = UserProfile.objects.all()
        ser = UserProfileSerializer(alluser, many=True)
        return Response({'user': ser.data})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'})
    
@api_view(['POST'])
def post_userprofile(request, id):
    try:
        user = User.objects.get(pk=id)
        data = request.data.copy()
        data['user'] = user.id
        ser = UserProfileSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'user':ser.data, 'message': 'UserProfile created successfully!'})
        else:
            return Response({'errors': ser.errors, 'message': 'Invalid data!'})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'}) 




class UserProfileAPIByID(APIView):
    def get(self, request, uid):
        try:
            user = UserProfile.objects.get(pk=uid)
            ser = UserProfileSerializer(user)
            return Response({'user': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'}) 
        
    def put(self, request, uid):
        try:
            user = UserProfile.objects.get(pk=uid)
            ser = UserProfileSerializer(user, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'user':ser.data, 'message': 'userProfile updated successfully!'})
            else:
                return Response({'errors': ser.errors, 'message': 'Invalid data!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'}) 
    
    def delete(self, request, uid):
        try:
            user = UserProfile.objects.get(pk=uid)
            user.delete()
            return Response({'message': 'UserProfile deleted'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'UserProfile not found'})









# ==============================
# Category APIs
# ==============================
class CategoryAPI(APIView):
    def get(self, request):
        try:
            allcategory = Category.objects.all()
            ser = CategorySerializer(allcategory, many=True)
            return Response({'category': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'}) 
        
    def post(self, request):
        try:
            ser = CategorySerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'category': ser.data, 'message': 'Category created successfully!'})
            else:
                return Response({'errors' : ser.errors, 'message': 'Invalid data!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'})


class CategoryAPIByID(APIView):
    def get(self, request, cid):
        try:
            category = Category.objects.get(pk=cid)
            ser = CategorySerializer(category)
            return Response({'category': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'}) 

    def put(self, request, cid):
        try:
            category = Category.objects.get(pk=cid)
            ser = CategorySerializer(category, request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'category': ser.data, 'message': 'Category updated successfully!'})
            else:
                return Response({'errors': ser.errors, 'message': 'Invalid data!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'}) 
    
    def delete(self, request, cid):
        try:
            category = Category.objects.get(pk=cid)
            category.delete()
            return Response({'message': 'Category deleted successfully!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Category not found!'})







# ==============================
# Product APIs
# ==============================
@api_view(['GET'])
def get_products(request):
    try:
        products = Product.objects.all()
        ser = ProductSerializer(products, many=True)
        return Response({'products': ser.data})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'}) 

@api_view(['POST'])
def post_products(request, cid):
    try:
        category = Category.objects.get(pk=cid)
        data = request.data.copy()
        data['category'] = category.id
        ser = ProductSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'product': ser.data, 'message': 'Product created successfully!'})
        else:
            return Response({'errors': ser.errors, 'message': 'Invalid data!'})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'})
    
@api_view(['PUT'])
def put_productByID(request, pid, cid):
    try:
        category = Category.objects.get(pk=cid)
        product = Product.objects.get(pk=pid)
        data = request.data.copy()
        data['category'] = category.id
        ser = ProductSerializer(product, data=data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'product': ser.data, 'message': 'Product updated successfully!'})
        else:
            return Response({'errors': ser.errors, 'message': 'Invalid data!'})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'}) 

class ProductAPIByID(APIView):
    def get(self,request, pid):
        try:
            products = Product.objects.get(pk=pid)
            ser = ProductSerializer(products)
            return Response({'products': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'})

    def delete(self, request, pid):
        try:
            product = Product.objects.get(pk=pid)
            product.delete()
            return Response({'message': 'Product deleted successfully!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'})





# ==============================
# Order APIs
# ==============================
@api_view(['GET'])
def get_orders(request):
    try:
        allorders = Order.objects.all()
        ser = OrderSerializer(allorders, many=True)
        return Response({'orders': ser.data})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'}) 

@api_view(['POST'])      
def post_orders(request, pid, id):
    try:
        user = User.objects.get(pk=id)
        products = Product.objects.get(pk=pid)
        data = request.data.copy()
        data['user'] = user.id
        data['product'] = products.id
        ser = OrderSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'order': ser.data, 'message': 'Order created successfully!'})
        else:
            return Response({'errors': ser.errors, 'message': 'Invalid data!'})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Something went wrong...'})

@api_view(['PUT'])
def put_orderByID(request, oid, pid, id):
    try:
        user = User.objects.get(pk=id)
        product = Product.objects.get(pk=pid)
        order = Order.objects.get(pk=oid)
        data = request.data.copy()
        data['user'] = user.id
        data['product'] = product.id
        ser = OrderSerializer(order, data=data, partial=True) 
        if ser.is_valid():
            ser.save()
            return Response({'order': ser.data, 'message': 'Order updated successfully!'})
        else:
            return Response({'errors': ser.errors, 'message': 'Invalid data!'})
    except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'})

class OrderDetailAPI(APIView):
    def get(self, request, oid):
        try:
            order = Order.objects.get(pk=oid)
            ser = OrderSerializer(order)
            return Response({'order': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'}) 
    
    def delete(self, request, oid):
        try:
            order = Order.objects.get(pk=oid)
            order.delete()
            return Response({'message': 'Order deleted successfully!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something went wrong...'})