# backend/services/api_service.py
import os
from typing import Optional
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from backend/.env if present
load_dotenv()

_supabase: Optional[Client] = None

def get_supabase() -> Optional[Client]:
    global _supabase
    if _supabase is not None:
        return _supabase
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        return None
    try:
        _supabase = create_client(url, key)
    except Exception:
        _supabase = None
    return _supabase

def insert_memory_log(log):
    try:
        client = get_supabase()
        if client is None:
            print("Supabase not configured; skipping insert.")
            return False
        res = client.table("memory_logs").insert({
            "thread_id": log.thread_id,
            "role": log.role,
            "content": log.content
        }).execute()
        # supabase-py returns a PostgrestResponse with .data and .error attributes
        return getattr(res, "error", None) is None
    except Exception as e:
        print("Insert error:", e)
        return False

def fetch_thread_logs(thread_id: str):
    try:
        client = get_supabase()
        if client is None:
            print("Supabase not configured; returning empty logs.")
            return []
        res = client.table("memory_logs").select("*").eq("thread_id", thread_id).order("created_at").execute()
        return getattr(res, "data", [])
    except Exception as e:
        print("Fetch error:", e)
        return []
