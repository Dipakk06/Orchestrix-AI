from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from courses.models import Course
from .logic import evaluate_course_progress


@login_required
def skill_tree(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    progress = evaluate_course_progress(request.user, course)
    return render(request, 'adaptive_engine/skill_tree.html', {'course': course, 'progress': progress})
