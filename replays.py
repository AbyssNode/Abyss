# replays.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/replays")
def replay_token_event(token: str = Query(...)):
    return {
        "token": token,
        "event": "Launch + first whale buy",
        "timestamp": "2025-05-28T14:45:00Z",
        "details": {
            "launch_price": 0.0012,
            "whale_buy": {"wallet": "0xDEAD...", "amount": 42000, "usd_value": 32000}
        }
    }
