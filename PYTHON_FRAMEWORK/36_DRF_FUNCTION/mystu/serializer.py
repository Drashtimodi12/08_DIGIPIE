from rest_framework import serializers
from mystu.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'      # Show all fields
        # fields = ['id', 'name']     # Show only selected fields
        # exclude=['name']        # Show all except some