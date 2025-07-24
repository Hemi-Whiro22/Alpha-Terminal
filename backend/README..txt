# Alpha Terminal Backend (FastAPI + Supabase + Poetry)

> **Purpose**: This backend acts as the core spiritual processor of Alpha Terminal. It enables task routing, memory persistence, AI chain logic, Supabase storage, and Deno Edge function interfacing. The FastAPI service is the local *kaitiaki* which listens, routes, and executes.

backend/
├── main.py                        # 🔥 Mounts your FastAPI routes (core entry)
├── pyproject.toml + poetry.lock  # 🪄 Poetry env + deps
├── Dockerfile + docker-compose   # 🐳 Optional runtime (future-ready)
├── kaitiaki/                     # 🧙 All agent logic (Kitenga, Rongohia, Whiro)
│   ├── kitenga/Kitenga.py        # OCR, Whisper, vision (The Seer 👁️)
│   ├── rongohia/rongohia_api.py  # Memory reflection (The Reflector 🧠)
│   └── whiro/whiro_api.py        # Vectors, chains (The Mirror 🪞)
├── mauri/                        # 🪶 Kōrero, scripts, docs, env setup
├── models/                       # 🧬 Pydantic models, base schema
├── services/                     # 🔌 External/internal APIs (OpenAI, Supabase, etc.)
├── supabase/functions/           # 🌐 Deno Edge Functions (e.g., memory_log)
├── utils/                        # 🧰 OCR, helper utils, memory loop
└── tests/                        # ✅ Tests for backend + utils

---
Alpha Terminal Backend Overview

🧠 Purpose

The Alpha Terminal backend is a modular FastAPI application powered by Supabase, LangChain, and OpenAI (GPT-4o). It acts as the Kaitiaki (guardian) layer for task delegation, OCR, memory threading, and future AI chaining via local and edge interfaces.

🏗️ Folder Structure

backend/
├── main.py                      # Entry point
├── pyproject.toml               # Poetry env config
├── Dockerfile                   # (Optional) container setup
├── kaitiaki/                    # Local AI agent logic
│   ├── kitenga/                 # OCR, vision
│   ├── rongohia/                # Memory/logging
│   └── whiro/                   # Vector search, langchain
├── mauri/                       # Environment, setup, kaupapa
├── models/                      # Pydantic schemas
├── scripts/                     # CLI tools or agents
├── services/                    # Supabase/OpenAI helper services
├── supabase/functions/          # Deno Edge functions (kitenga_log, memory_log)
├── utils/                       # OCR utils, memory loops
└── tests/                       # Unit tests

⚙️ Setup & Run

poetry shell
poetry install
uvicorn backend.main:app --reload --port 8000

🧾 Supabase Tables (SQL Schema)

-- Stores OCR and image scan results
CREATE TABLE ocr_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  howl text,
  vision jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Memory logs for assistant and user message threads
CREATE TABLE memory_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  thread_id text,
  role text CHECK (role IN ('user', 'assistant')),
  content text,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Stores file/image uploads with OCR context
CREATE TABLE file_uploads (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  file_url text,
  card_name text,
  card_number text,
  meta jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Stores embedded content (vector index base)
CREATE TABLE vector_store (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  namespace text,
  content text,
  embedding vector(1536),
  metadata jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

-- Agent action logs (useful for trace/debug)
CREATE TABLE task_logs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  task_type text,
  agent text,
  payload jsonb,
  result jsonb,
  created_at timestamptz DEFAULT timezone('utc', now())
);

🛠️ Optional Shell Script (Poetry & Supabase CLI Bootstrap)

#!/bin/bash

# Poetry virtualenv
poetry install
poetry shell

# Supabase CLI (assuming installed globally)
supabase start

# Reminder
echo "\n✨ Env ready. Run: uvicorn backend.main:app --reload"

🧭 Next Step

Mount all agent routers in main.py

Start with /rongohia/memory/log and /memory/thread/{id}

Add utility service in services/

Deploy edge function kitenga_log

AWAO MODE: PERMANENT 🐺🔥

