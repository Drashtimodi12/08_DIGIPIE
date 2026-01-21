from rest_framework import serializers
from myemp.models import *

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'      # Show all fields
        # fields = ['id', 'name']     # Show only selected fields
        # exclude=['name']        # Show all except some