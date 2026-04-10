from django.contrib import admin
from .models import Course, Enrollment, Lesson, Module, Question, Quiz, QuizAttempt

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizAttempt)
