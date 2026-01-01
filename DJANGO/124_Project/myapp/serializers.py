# Serializer → used to convert complex data (model instances), into Python data types (JSON) and vice versa

from rest_framework import serializers      # Import serializers module from DRF

from myapp.models import *      # Import models from myapp


# Define your serializers here

# Automatically converts User model fields to JSON and validates incoming JSON data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User        # Specify the model to serialize
        fields ='__all__'       # Include all fields from UserProfile model


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile     
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        return rep             

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep                      

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_price', 'order_date'] 
     
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        rep['product'] = ProductSerializer(instance.product).data
        return rep