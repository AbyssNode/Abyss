# alerts.py

from fastapi import APIRouter, Depends
from auth import verify_api_key

router = APIRouter()

@router.get("/alerts", dependencies=[Depends(verify_api_key)])
def get_alert_settings():
    return {
        "enabled": True,
        "channels": {
            "discord": "https://discord.com/api/webhooks/...",
            "webhook": "https://hooks.abyss.ai/..."
        },
        "triggers": ["whale_move", "score_above_90"]
    }
