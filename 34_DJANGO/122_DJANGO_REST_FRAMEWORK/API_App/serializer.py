# Serializer:=  A serializer in Django REST Framework converts Django model instances into JSON and validates JSON data before saving it into the database.
# When to use?:=    Building REST APIs, Sending data to frontend
# DRF serializers module
from rest_framework import serializers
from API_App.models import *


# ------------------------
# Stuent
# ------------------------
# ModelSerializer automatically creates serializer fields (Adds validation, Adds create() and update() methods) based on the Django model fields
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        # Which model this serializer is for
        model = Student
        # '__all__' means include ALL fields from Student model
        fields = '__all__'

        # If you want only specific fields, use this:
        # fields = ['id', 'name']

        # If you want to exclude some fields, use this:
        # exclude = ['name']



# ------------------------
# Employee
# ------------------------
class EmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


# ------------------------
# Product
# ------------------------
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"