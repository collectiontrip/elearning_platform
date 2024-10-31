from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import User, Course,  Enrollment, Certification, OTP, Item, Content
from .permissions import IsStudent, IsInstructorOrAdmin
from .serializers import UserSerializer, CourseSerializer,  EnrollmentSerializer, CertificationSerializer, ItemSerializer, ContentSerializer
from .utils import generate_otp, send_otp_email
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User(
                username= serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                role=serializer.validated_data['role']
            )
            user.set_password(serializer.validated_data['password'])
            user.save()
            
           
            
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginView(APIView):
    def post(self, reuqest):
        username = reuqest.data.get('username')
        password = reuqest.data.get('password')
        
        
        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"message": "Login successfull!"}, status=status.HTTP_200_OK)
            
                
        return Response(
            {
                "error": "Invalid credentials"
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
    def get_serializer_context(self):
        return {'request': self.request}
    

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer 

    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsStudent]  

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
     
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticated, IsInstructorOrAdmin]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    