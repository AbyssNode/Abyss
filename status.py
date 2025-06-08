# status.py

from fastapi import APIRouter
from datetime import datetime
import os

router = APIRouter()
start_time = datetime.utcnow()

@router.get("/status")
def get_status():
    uptime = (datetime.utcnow() - start_time).total_seconds()
    logs_exist = os.path.exists("abyss-core/abyss.log")
    
    return {
        "status": "online",
        "uptime_seconds": round(uptime),
        "log_file": "available" if logs_exist else "missing"
    }
