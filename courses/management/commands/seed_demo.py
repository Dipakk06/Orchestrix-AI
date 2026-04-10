from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from adaptive_engine.models import ConceptDependency, ConceptNode
from courses.models import Course, Lesson, Module, Question, Quiz, QuizAttempt
from users.models import StudentProfile


class Command(BaseCommand):
    help = 'Seed demo Edu-Net data'

    def handle(self, *args, **options):
        User = get_user_model()
        teacher, _ = User.objects.get_or_create(username='teacher', defaults={'role': 'teacher'})
        teacher.set_password('teacher123')
        teacher.save()

        student, _ = User.objects.get_or_create(username='student', defaults={'role': 'student'})
        student.set_password('student123')
        student.save()

        profile, _ = StudentProfile.objects.get_or_create(user=student)
        profile.xp_points = 180
        profile.streak_days = 5
        profile.save()

        course, _ = Course.objects.get_or_create(title='Intro to AI', teacher=teacher, defaults={'description': 'Adaptive AI foundations.'})
        m1, _ = Module.objects.get_or_create(course=course, title='Math Basics', order=1)
        m2, _ = Module.objects.get_or_create(course=course, title='Neural Foundations', order=2)

        l1, _ = Lesson.objects.get_or_create(module=m1, title='Matrix Multiplication', order=1, defaults={'summary_video_url': 'https://www.youtube.com/watch?v=OMA2Mwo0aZg'})
        l2, _ = Lesson.objects.get_or_create(module=m2, title='Neural Networks Intro', order=1, defaults={'summary_video_url': 'https://www.youtube.com/watch?v=aircAruvnKk'})

        q1, _ = Quiz.objects.get_or_create(lesson=l1, defaults={'title': 'Matrix Quiz'})
        q2, _ = Quiz.objects.get_or_create(lesson=l2, defaults={'title': 'NN Quiz'})
        Question.objects.get_or_create(quiz=q1, prompt='What is matrix dimension compatibility?', topic='Matrices', correct_answer='rule')
        Question.objects.get_or_create(quiz=q2, prompt='What does a neuron output?', topic='Neural Nets', correct_answer='activation')

        n1, _ = ConceptNode.objects.get_or_create(lesson=l1, defaults={'title': 'Matrix Multiplication', 'remediation_video_url': 'https://www.youtube.com/watch?v=OMA2Mwo0aZg'})
        n2, _ = ConceptNode.objects.get_or_create(lesson=l2, defaults={'title': 'Neural Networks', 'remediation_video_url': 'https://www.youtube.com/watch?v=aircAruvnKk'})
        ConceptDependency.objects.get_or_create(prerequisite=n1, target=n2)

        QuizAttempt.objects.get_or_create(student=student, quiz=q1, defaults={'score': 45})
        QuizAttempt.objects.get_or_create(student=student, quiz=q2, defaults={'score': 88})

        self.stdout.write(self.style.SUCCESS('Demo data created: student/student123, teacher/teacher123'))
