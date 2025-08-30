# backend/main.py
from fastapi import FastAPI
from backend.kaitiaki.kitenga.kitengas_api import router as kitenga_router
from backend.kaitiaki.rongohia.rongohia_api import router as rongohia_router
from backend.kaitiaki.whiro.whiro_api import router as whiro_router
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
