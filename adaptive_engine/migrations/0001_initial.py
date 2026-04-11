from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency('users.User'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('remediation_video_url', models.URLField(blank=True)),
                ('lesson', models.OneToOneField(on_delete=models.deletion.CASCADE, related_name='concept_node', to='courses.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptDependency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prerequisite', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='unlocks', to='adaptive_engine.conceptnode')),
                ('target', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='requires', to='adaptive_engine.conceptnode')),
            ],
            options={
                'unique_together': {('prerequisite', 'target')},
            },
        ),
        migrations.CreateModel(
            name='ConceptMastery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('unlocked', models.BooleanField(default=False)),
                ('fast_track', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('node', models.ForeignKey(on_delete=models.deletion.CASCADE, to='adaptive_engine.conceptnode')),
                ('student', models.ForeignKey(on_delete=models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'unique_together': {('student', 'node')},
            },
        ),
    ]
