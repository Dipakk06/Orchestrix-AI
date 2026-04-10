from collections import defaultdict
from courses.models import QuizAttempt
from .models import ConceptDependency, ConceptMastery


LOCK_THRESHOLD = 50
FAST_TRACK_THRESHOLD = 90


def update_mastery_from_latest_quiz(student, node):
    quiz = getattr(node.lesson, 'quiz', None)
    score = 0
    if quiz:
        attempt = QuizAttempt.objects.filter(student=student, quiz=quiz).first()
        if attempt:
            score = attempt.score

    mastery, _ = ConceptMastery.objects.get_or_create(student=student, node=node)
    mastery.score = score
    mastery.fast_track = score >= FAST_TRACK_THRESHOLD
    mastery.save()
    return mastery


def evaluate_course_progress(student, course):
    nodes = []
    for module in course.modules.all():
        for lesson in module.lessons.all():
            if hasattr(lesson, 'concept_node'):
                nodes.append(lesson.concept_node)
    dependencies = ConceptDependency.objects.filter(target__in=nodes).select_related('prerequisite', 'target')
    prerequisite_map = defaultdict(list)
    for dep in dependencies:
        prerequisite_map[dep.target_id].append(dep.prerequisite)

    result = []
    for node in nodes:
        mastery = update_mastery_from_latest_quiz(student, node)
        prereqs = prerequisite_map.get(node.id, [])
        unlocked = all(update_mastery_from_latest_quiz(student, p).score >= LOCK_THRESHOLD for p in prereqs)
        if not prereqs:
            unlocked = True

        mastery.unlocked = unlocked
        mastery.save(update_fields=['unlocked', 'updated_at'])
        result.append({
            'node': node,
            'score': mastery.score,
            'unlocked': unlocked,
            'fast_track': mastery.fast_track,
            'needs_remediation': mastery.score < LOCK_THRESHOLD,
        })
    return result
