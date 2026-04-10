from collections import Counter
from django.db.models import Avg
from adaptive_engine.ml_models import predict_failure_probability
from courses.models import QuizAttempt, Question
from users.models import StudentProfile, UserActivity


def build_dashboard_context(user):
    attempts = QuizAttempt.objects.filter(student=user)
    avg_score = attempts.aggregate(v=Avg('score'))['v'] or 0
    weekly_logins = UserActivity.objects.filter(user=user, action='login').count()
    avg_video_completion = 0.8
    risk_probability = predict_failure_probability(avg_score, weekly_logins, avg_video_completion)

    topic_wrong_counts = Counter()
    for attempt in attempts.select_related('quiz')[:30]:
        for question in Question.objects.filter(quiz=attempt.quiz):
            if attempt.score < 100:
                topic_wrong_counts[question.topic] += 1

    weakness_labels = list(topic_wrong_counts.keys()) or ['Algebra', 'Geometry', 'Logic']
    weakness_values = list(topic_wrong_counts.values()) or [2, 1, 3]

    profile, _ = StudentProfile.objects.get_or_create(user=user)
    leaderboard_rank = max(1, StudentProfile.objects.filter(xp_points__gt=profile.xp_points).count() + 1)

    return {
        'avg_score': round(avg_score, 2),
        'risk_probability': risk_probability,
        'xp_points': profile.xp_points,
        'streak_days': profile.streak_days,
        'leaderboard_rank': leaderboard_rank,
        'weakness_labels': weakness_labels,
        'weakness_values': weakness_values,
    }
