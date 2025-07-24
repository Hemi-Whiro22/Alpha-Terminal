# backend/main.py
from fastapi import FastAPI
from kaitiaki.kitenga.kitengas_api import router as kitenga_router
from kaitiaki.rongohia.rongohia_api import router as rongohia_router
from kaitiaki.whiro.whiro_api import router as whiro_router
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize FastAPI app

app = FastAPI()

# Mount all the kaitiaki routes
app.include_router(kitenga_router, prefix="/kitenga", tags=["Kitenga"])
app.include_router(rongohia_router, prefix="/rongohia", tags=["Rongohia"])
app.include_router(whiro_router, prefix="/whiro", tags=["Whiro"])
# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"} 
    # Ensure environment variables are loaded
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase environment variables are not set correctly.")
# Ensure the necessary environment variables are loaded
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
if not SUPABASE_SERVICE_ROLE_KEY:
    raise ValueError("Supabase service role key is not set.")
# Ensure the necessary environment variables are loaded
SUPABASE_EDGE_URL = f"{SUPABASE_URL}/rest/v1/whiro"
headers = {
    "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
    "Content-Type": "application/json"
}       
}