# Edu-Net (Adaptive Learning Demo)

Edu-Net is a working Django web application that demonstrates adaptive learning logic:

- Custom users (student/teacher)
- Course/module/lesson structure
- Adaptive concept locking + fast-track logic
- Risk radar score widget
- Weakness heatmap using Chart.js
- Gamified XP + leaderboard rank

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

Then open:
- `/accounts/login/`
- `/dashboard/`
- `/courses/`

## Architecture

- `users/` – custom auth model, student profile, activity logs
- `courses/` – content hierarchy + quiz data
- `adaptive_engine/` – concept graph dependencies and unlock logic
- `analytics_app/` – risk and weakness dashboards
