# backend/services/api_service.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv
# Load environment variables


load_dotenv()
# Ensure environment variables are set
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise ValueError("Supabase environment variables are not set correctly.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def insert_memory_log(log):
    try:
        res = supabase.table("memory_logs").insert({
            "thread_id": log.thread_id,
            "role": log.role,
            "content": log.content
        }).execute()
        return not res.get("error")
    except Exception as e:
        print("Insert error:", e)
        return False

def fetch_thread_logs(thread_id: str):
    try:
        res = supabase.table("memory_logs").select("*").eq("thread_id", thread_id).order("created_at").execute()
        return res.data
    except Exception as e:
        print("Fetch error:", e)
        return []
