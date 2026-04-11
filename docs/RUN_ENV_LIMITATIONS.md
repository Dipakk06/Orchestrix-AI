# Running Edu-Net when package download fails

If `./run` fails while installing `Django==5.2.7`, your environment is blocking access to package repositories.

## What you can do

### 1) Run locally on your own machine (fastest)

```bash
git clone <your-repo-url>
cd Orchestrix-AI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Then open `http://127.0.0.1:8000/accounts/login/`.

### 2) Use a corporate/internal Python mirror

If you have an internal package mirror, set it before install:

```bash
pip install -r requirements.txt --index-url <internal-pypi-url>
```

### 3) Use a wheelhouse (offline artifacts)

On a machine with internet:

```bash
mkdir wheelhouse
pip download -r requirements.txt -d wheelhouse
```

Copy `wheelhouse/` to the restricted environment, then:

```bash
pip install --no-index --find-links wheelhouse -r requirements.txt
```

### 4) Verify install before running

```bash
python -c "import django; print(django.get_version())"
```

If this prints a version, run:

```bash
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```
