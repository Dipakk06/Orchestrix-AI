from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentProfile, User, UserActivity

admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(UserActivity)
