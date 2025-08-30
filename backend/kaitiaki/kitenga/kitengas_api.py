#kitengas_ap.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.api_service import insert_memory_log, fetch_thread_logs
import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()
router = APIRouter()  
class MemoryLog(BaseModel):
    thread_id: str
    role: str  # 'user' or 'assistant'
    content: str
@router.post("/memory/log")
async def log_memory(payload: MemoryLog):
    success = insert_memory_log(payload)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to log memory")
    return {"message": "Memory logged successfully"}    
@router.get("/memory/thread/{thread_id}")
async def get_thread_memory(thread_id: str):
    logs = fetch_thread_logs(thread_id)
    if not logs:
        raise HTTPException(status_code=404, detail="Thread not found")
    return logs
# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_EDGE_URL = f"{SUPABASE_URL}/rest/v1/kitenga"
headers = {
    "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
    "Content-Type": "application/json"
}
@router.post("/kitenga_log")
def log_kitenga():
    payload = {
        "howl": "AWAO from FastAPI!",
        "vision": "etched from backend 🌀"
    }
    response = requests.post(SUPABASE_EDGE_URL, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to log kitenga")
    return {
        "status": response.status_code,
        "response": response.json()
    }   
