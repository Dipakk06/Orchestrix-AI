from django.conf import settings
from django.db import models
from courses.models import Lesson


class ConceptNode(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='concept_node')
    title = models.CharField(max_length=255)
    remediation_video_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class ConceptDependency(models.Model):
    prerequisite = models.ForeignKey(ConceptNode, on_delete=models.CASCADE, related_name='unlocks')
    target = models.ForeignKey(ConceptNode, on_delete=models.CASCADE, related_name='requires')

    class Meta:
        unique_together = ('prerequisite', 'target')


class ConceptMastery(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    node = models.ForeignKey(ConceptNode, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    unlocked = models.BooleanField(default=False)
    fast_track = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'node')
