# exitwatch.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/exitwatch")
def get_exit_watchlist():
    return {
        "tokens_whales_are_exiting": [
            {"token": "DriftFi", "exit_volume_usd": 72000},
            {"token": "SinkCap", "exit_volume_usd": 51000},
            {"token": "NullMoon", "exit_volume_usd": 46000}
        ],
        "timestamp": "2025-06-14T18:00:00Z"
    }
