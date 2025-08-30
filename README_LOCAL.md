# Alpha Terminal backend (non-Docker run)

Quick start (Linux/macOS):

1) Create a virtualenv and install deps

   python -m venv .venv
   source .venv/bin/activate
   pip install -U pip
   pip install -r backend/requirements.txt

2) Configure env

   cp backend/.env.example backend/.env
   # edit backend/.env and set SUPABASE_* keys

3) Run API

   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

Makefile shortcuts:
- make install  # venv + deps
- make env      # copy .env.example if missing
- make dev      # run with reload on :8000
- make run      # run without reload

Health check: http://localhost:8000/health

Routes:
- /kitenga
- /rongohia
- /whiro
