"""Lightweight risk model fallback for demos.

If sklearn artifacts are absent, a transparent heuristic model is used.
"""


def predict_failure_probability(avg_quiz_score, weekly_logins, avg_video_completion):
    score_risk = max(0, (70 - avg_quiz_score) / 70)
    login_risk = max(0, (4 - weekly_logins) / 4)
    video_risk = max(0, (0.75 - avg_video_completion) / 0.75)
    risk = (0.55 * score_risk) + (0.25 * login_risk) + (0.20 * video_risk)
    return min(round(risk * 100, 2), 99.0)
