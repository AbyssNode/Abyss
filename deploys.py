# deploys.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/deploys")
def get_recent_deploys(hours: int = Query(24)):
    return {
        "window_hours": hours,
        "new_tokens": [
            {"token": "NebulaX", "deployed_at": "2025-06-14T03:12:00Z"},
            {"token": "OceanPulse", "deployed_at": "2025-06-14T06:47:00Z"}
        ],
        "total_detected": 74
    }
