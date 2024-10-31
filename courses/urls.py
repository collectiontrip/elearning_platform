from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet,  RegisterView, LoginView, EnrollmentViewSet, UserViewSet, CertificationViewSet, ItemViewSet, ContentViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'content', ContentViewSet)
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register('users', UserViewSet, basename='user')
router.register(r'certifications', CertificationViewSet, basename='certification')
router.register(r'items', ItemViewSet, basename='item')


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name= 'register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
