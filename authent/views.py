#from django.contrib.auth.models import Student
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Generate JWT Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# User Registration
@api_view(['POST'])
def register_user(request):
    
    form = Student(request.POST)
    if not form.is_valid():
        return Response({"error": form.errors}, status=400)

    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    age = request.data.get('age')
    father_name = request.data.get('father_name')
    class_name = request.data.get('class_name')
    
    createUserData = {
        "name":name,
        "email":email,
        "password":password,
        "age":age,
        "father_name":father_name,
        "class_name":class_name
    }

    if not name or not email or not password:
        return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

    if Student.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    #user = Student.objects.create_user(name=name, email=email, password=password)
    user = Student.objects.create_user(**createUserData)
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

# User Login
@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(email=email, password=password)

    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'message': 'This is a protected view'}, status=status.HTTP_200_OK)
