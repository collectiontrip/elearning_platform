from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Course,  Quiz, Question, Enrollment, Certification, OTP, Item, Content


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        
    )
    
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields =  ('username', 'email', 'first_name', 'last_name')
    
class ContentInline(admin.TabularInline):
    model = Content
    extra = 1    

    
class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 1
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'price', 'created_at')
    list_filter = ('instructor', 'created_at')
    search_fields = ('title', 'description', 'instructor__username')
    inlines = [ QuizInline, ContentInline]
    
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'type', 'created_at')
    list_filter = ('type', 'course')
    search_fields = ('title',)
       
@admin.register(Enrollment)
class EnrollMentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('enrolled_at',)
    search_fields = ('student__username', 'course__title')
    
    
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')
    inlines = [QuestionInline]
 
 
  
@admin.register(Certification)
class CerttificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'issued_at')
    list_filter = ('issued_at',)
    search_fields = ('user__username', 'title')

def resend_otp(modeladmin, request, queryset):
    for otp in queryset:
        print(f"Resending OTP: {otp.code} to {otp.user.email}")  # Replace with actual email logic

resend_otp.short_description = "Resend selected OTPs"

    
@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'created_at', 'is_valid')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    actions = [resend_otp]
    

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)