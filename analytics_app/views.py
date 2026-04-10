from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import UserActivity
from .services import build_dashboard_context


@login_required
def dashboard_home(request):
    UserActivity.objects.create(user=request.user, action='login')
    context = build_dashboard_context(request.user)
    context['daily_goal'] = 'Focus on your weakest concept to reduce your risk score.'
    return render(request, 'dashboard/home.html', context)
