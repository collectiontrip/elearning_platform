from rest_framework import serializers
from .models import User, Course,  Enrollment, Certification, Item, Content


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
       model = User
       fields = ['id', 'username', 'email', 'role', 'password']
       extra_kwargs = {'password': {'write_only': True}}
       
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            role=validated_data.get('role', 'student')
        )
        return user
    def update(self, instance, validated_data):
        validated_data.pop('instructor', None)
        return super().update(instance, validated_data)
       

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'price', 'created_at']
        read_only_fields = ['instructor', 'created_at']
        
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['instructor'] = request.user
        return super().create(validated_data)
        
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content  
        fields = '__all__'
           
    
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at'] 
       
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification  
        fields = ['id', 'user', 'title', 'description', 'issued_at']     
   
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'