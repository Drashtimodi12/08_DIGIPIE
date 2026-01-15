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
    AllowAny,                # AllowAny        → anyone can access API
    BasePermission
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

import razorpay








# Create your views here

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff

# ==============================
# User
# ==============================
class UserRegistrationAPIView(APIView):
    def post(self, request):
        try:
            ser = UserSerializer(data=request.data)
            if ser.is_valid():
                user = ser.save()
                return Response({'message': 'User Registered successfully!', 'user_id': user.id})
            else:
                return Response({'errors':ser.errors})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'}) 


# ==============================
# Category
# ==============================
class CategoryAPI(APIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(), IsStaffUser()]
        return [AllowAny()]


    def get(self, request, pk=0):
        try:
            if pk == 0:   
                allcategory = Category.objects.all()
                ser = CategorySerializer(allcategory, many=True)
                return Response({'allcategory': ser.data})    
            else:
                category = Category.objects.get(pk=pk)
                ser = CategorySerializer(category)
                return Response({'category': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})

    def post(self, request):
        try:
            ser = CategorySerializer(data=request.data) 
            if ser.is_valid():
                ser.save()
                return Response({'category': ser.data})
            else:
                return Response({'errors': ser.errors})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})
        
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            ser = CategorySerializer(category, data=request.data, partial=True) 
            if ser.is_valid():
                ser.save()
                return Response({'category': ser.data})
            else:
                return Response({'errors': ser.errors, 'message': 'Something wents wrong!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})
        
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({'message': 'Category deleted successfully!'}) 
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})

# ==============================
# Product
# ==============================
class ProductAPI(APIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(), IsStaffUser()]
        return [AllowAny()]

    def get(self, request, pk=0):
        try:
            if pk == 0:   
                allproduct = Product.objects.all()
                ser = ProductSerializer(allproduct, many=True)
                return Response({'product': ser.data})    
            else:
                product = Product.objects.get(pk=pk)
                ser = ProductSerializer(product)
                return Response(ser.data)
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})


    def post(self, request):
        try:
            ser = ProductSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'product':ser.data})
            else:
                return Response({'errors': ser.errors})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})

    
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            ser = ProductSerializer(product, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({'product':ser.data})
            else:
                return Response({'errors': ser.errors})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})
        
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'message': 'Product deleted successfully'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})


class ProductByCategoryAPIView(APIView):    
    def get(self, request, category_id):
        try:
            products = Product.objects.filter(category_id=category_id)
            ser = ProductSerializer(products, many=True)
            return Response({'ProductByCategory': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})


class ProductSearchAPIView(APIView):
    def get(self, request):
        try:
            query = request.query_params.get('q', '')
            if query:
                products = Product.objects.filter(name__istartswith=query)        #name__icontains find all over name and name__startswith find name from starting
                ser = ProductSerializer(products, many=True)    
                return Response(ser.data)
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})
        

# ==============================
# Cart
# ==============================
class CartAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        

    def get(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response({'errors': ' Authentication Required!'})
            else:
                allcart = Cart.objects.filter(user=user)
                ser = CartSerializer(allcart, many=True)
                return Response({'cart': ser.data})    
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})


    def post(self, request):
        try:
            user = request.user     # Get logged-in user
            if not user.is_authenticated:           # Check if user is authenticated
                return Response({'errors': ' Authentication Required!'})
            else:
                product_id = request.data.get('product')        # Get product id from request body
                isExist = Cart.objects.filter(product_id=product_id, user_id=user.id).exists()      # Check if product already exists in user's cart
                if isExist:
                    return Response({'error': 'Product already exists in cart'}, status=400)

                request.data['user'] = user.id      # Attach logged-in user id to request data

                ser = CartSerializer(data=request.data)
                if ser.is_valid():
                    ser.save()
                    return Response({'cart': ser.data})
                else:
                    return Response({'errors': ser.errors, 'message':'Something wents wrong!'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})


    def delete(self, request, pk):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response({'error': 'Authentication required'})
            else:
                cart_item = Cart.objects.get(pk=pk, user=user)
                cart_item.delete()
                return Response({'message': 'Cart item deleted successfully'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})



class ChangeQtyAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method in ['PUT']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def put(self, request, pk):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response({'error': 'Authentication required'})
            else:
                cart_item = Cart.objects.get(pk=pk, user=user)
                request.data['quantity'] = cart_item.quantity + request.data['quantity']   # Default to current quantity if not provided
                if request.data['quantity'] < 1:
                    cart_item.delete()
                    return Response({'error': 'Quantity must be at least 1'})
                else:
                    ser = CartSerializer(cart_item, data=request.data, partial=True)
                    if ser.is_valid():
                        ser.save()
                        return Response({'cart': ser.data})
                    else:
                        return Response({'errors': ser.errors})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})







# ==============================
# Order
# ==============================
class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        try: 
            user = request.user
            if not user.is_authenticated:
                return Response({'error': 'Authentication required'})
            else:
                orders = Order.objects.filter(user=user).prefetch_related("items")
                if not orders.exists():
                    return Response({'message': 'No orders found'})
                else:
                    ser = OrderSerializer(orders , many=True)
                    return Response(ser.data)
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})

    def post(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return Response({'error': 'Authentication required'})
            else:
                cart_items = Cart.objects.filter(user=user)
                if not cart_items.exists():
                    return Response({'error': 'Cart is empty'})
                else:
                    total_price = sum(item.product.price * item.quantity for item in cart_items)
                    request.data['user'] = user.id
                    request.data['total_price'] = total_price
                    ser = OrderSerializer(data=request.data)
                    if ser.is_valid():
                        ser.save()
                        # Create OrderItems for each cart item
                        order = ser.instance
                        for item in cart_items:
                            OrderItem.objects.create(
                                order=order,
                                product=item.product,
                                quantity=item.quantity,
                                price=item.product.price
                            )
                        # Clear the cart after order creation
                        cart_items.delete()
                        return Response(ser.data)
                    else:
                        return Response({'errors': ser.errors})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Something wents wrong!'})
    

    
  
# ==============================
# OrderItem
# ==============================


