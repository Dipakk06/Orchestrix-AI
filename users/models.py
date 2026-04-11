from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    learning_style = models.CharField(max_length=100, blank=True)
    xp_points = models.PositiveIntegerField(default=0)
    streak_days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} profile'


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=120)
    metadata = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username} - {self.action}'
