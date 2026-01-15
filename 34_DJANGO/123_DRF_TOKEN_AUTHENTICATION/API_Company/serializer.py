from rest_framework import serializers
from API_Company.models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department'] = DepartmentSerializer(instance.department).data
        return representation