      
from rest_framework import serializers
from .models import Food, Delivery, User, OrderFood, Admin

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} # Hash password on creation

    def create(self, validated_data):  # Hash the password before saving
        password = validated_data.pop('password')
        user = User(**validated_data) # Changed 'user' to 'User' to match the Model
        user.set_password(password)  # Hash the password
        user.save()
        return user

class OrderFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

    