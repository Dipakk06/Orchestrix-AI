from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency('users.User'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('teacher', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='courses_taught', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=1)),
                ('course', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='modules', to='courses.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro_video_url', models.URLField(blank=True)),
                ('summary_video_url', models.URLField(blank=True)),
                ('order', models.PositiveIntegerField(default=1)),
                ('module', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='lessons', to='courses.module')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='enrollments', to='courses.course')),
                ('student', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='enrollments', to='users.user')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('lesson', models.OneToOneField(on_delete=models.deletion.CASCADE, related_name='quiz', to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
                ('quiz', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='questions', to='courses.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(help_text='Percent score, 0-100')),
                ('taken_at', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=models.deletion.CASCADE, to='courses.quiz')),
                ('student', models.ForeignKey(on_delete=models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'ordering': ['-taken_at'],
            },
        ),
    ]
