# Edu-Net (Adaptive Learning Demo)

Edu-Net is a Django web application that demonstrates adaptive learning logic with a thesis-friendly scope:

- Custom users (student/teacher)
- Course/module/lesson structure
- Adaptive concept locking + fast-track logic
- Risk radar score widget
- Weakness heatmap using Chart.js
- Gamified XP + leaderboard rank

## Quick Start

### Option 1: One command (recommended)

```bash
./run
```

(`./run` is a tiny wrapper around `./scripts/run_local.sh`.)

This command will:
1. Create a virtual environment (`.venv`) if missing
2. Install dependencies (if not already installed)
3. Run migrations
4. Seed demo data
5. Start the dev server on `127.0.0.1:8000`

### Option 2: Manual setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

## Demo Accounts

After `seed_demo`, use:

- Student: `student` / `student123`
- Teacher: `teacher` / `teacher123`

## App URLs

- `/accounts/login/`
- `/dashboard/`
- `/courses/`
- `/adaptive/skill-tree/`


Need help with restricted environments? See `docs/RUN_ENV_LIMITATIONS.md`.

## Troubleshooting

If installation fails with proxy/network errors:

- Ensure `HTTP_PROXY` and `HTTPS_PROXY` are correctly configured for your environment.
- If outbound internet is blocked, dependency installation from PyPI will fail. In that case, install dependencies from an internal mirror or prebuilt wheel cache.

## Architecture

- `users/` – custom auth model, student profile, activity logs
- `courses/` – content hierarchy + quiz data
- `adaptive_engine/` – concept graph dependencies and unlock logic
- `analytics_app/` – risk and weakness dashboards
