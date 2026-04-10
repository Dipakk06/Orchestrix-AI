from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Course
from adaptive_engine.logic import evaluate_course_progress


@login_required
def course_list(request):
    courses = Course.objects.all().prefetch_related('modules__lessons')
    return render(request, 'courses/course_list.html', {'courses': courses})


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course.objects.prefetch_related('modules__lessons'), pk=course_id)
    progress = evaluate_course_progress(request.user, course)
    return render(request, 'courses/course_detail.html', {'course': course, 'progress': progress})
