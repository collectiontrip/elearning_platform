from django.contrib import admin
from .models import User, Course, Lesson, Enrollment, Quiz, Question, Enrollment, Certification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']
    list_filter = ['role']

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Certification)