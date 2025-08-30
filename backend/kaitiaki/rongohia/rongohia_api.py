# backend/kaitiaki/rongohia/rongohia_api.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.api_service import insert_memory_log, fetch_thread_logs
import os
from dotenv import load_dotenv
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
    return logs
