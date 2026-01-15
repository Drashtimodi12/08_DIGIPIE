# Serializer → used to convert complex data (model instances), into Python data types (JSON) and vice versa

from rest_framework import serializers      # Import serializers module from DRF

from myapp.models import *      # Import models from myapp.models

# Define your serializers here

# ==============================
# User
# ==============================
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for Django's built-in User model.
    Converts User model instances into JSON and vice versa.
    """

    class Meta:
        model = User                      # Specify the model to serialize
        fields = '__all__'               # Include all fields of User model

    def create(self, validated_data):
        """
        Custom create method to handle user registration.
        Ensures the password is stored in encrypted (hashed) format.
        """
        # Create user using Django's built-in create_user method. This automatically handles username, email, and password hashing
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])           # Explicitly hashing password again (optional but safe)
        user.save()
        return user


# ==============================
# Category
# ==============================
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category        
        fields = '__all__'      


# ==============================
# Product
# ==============================
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation 

    

# ==============================
# Cart
# ==============================
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        return representation

# ==============================
# OrderItem
# ==============================
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        representation['order'] = OrderSerializer(instance.order).data
        return representation
     

# ==============================
# Order
# ==============================
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customize the representation of the Order model to include product details.
        """
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        return representation