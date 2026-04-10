#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

VENV_DIR="${VENV_DIR:-.venv}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "[ERROR] Python interpreter '$PYTHON_BIN' not found."
  exit 1
fi

if [[ ! -d "$VENV_DIR" ]]; then
  "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

if ! python -c "import django" >/dev/null 2>&1; then
  echo "[INFO] Installing dependencies from requirements.txt..."
  if ! pip install -r requirements.txt; then
    echo "[ERROR] Dependency installation failed."
    echo "        If your environment requires a proxy, export HTTP_PROXY/HTTPS_PROXY first."
    echo "        If your environment blocks network access, install Django manually in this venv and rerun."
    exit 1
  fi
fi

python manage.py migrate
python manage.py seed_demo

echo "[INFO] Starting development server at http://127.0.0.1:8000"
python manage.py runserver 127.0.0.1:8000
