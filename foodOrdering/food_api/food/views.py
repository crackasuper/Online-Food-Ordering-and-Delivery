from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .models import Food, Delivery, User, OrderFood, Admin
from .serializers import FoodSerializer, DeliverySerializer, UserSerializer, OrderFoodSerializer, AdminSerializer
from django.contrib.auth import authenticate
from django.db import IntegrityError

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response({"error": "A user with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderFoodList(generics.ListCreateAPIView):
    queryset = OrderFood.objects.all()
    serializer_class = OrderFoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderFoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderFood.objects.all()
    serializer_class = OrderFoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AdminList(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            return Response({"error": "A Admin with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Authentication Views

@api_view(['POST'])
@permission_classes([permissions.AllowAny])  # Allow anyone to access login
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'firstName': user.firstName})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated]) # Only authenticated users can logout
def user_logout(request):
    try:
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])  # Allow anyone to access login
def admin_login(request):
    firstName = request.data.get('firstName')
    password = request.data.get('password')

    admin = authenticate(request, firstName=firstName, password=password)

    if admin is not None:
        token, _ = Token.objects.get_or_create(user=admin)
        return Response({'token': token.key, 'firstName': admin.firstName})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated]) # Only authenticated users can logout
def admin_logout(request):
    try:
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    