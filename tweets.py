# tweets.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/tweets")
def get_token_mentions(token: str = Query(...)):
    return {
        "token": token,
        "mentions": [
            {"user": "@whaletrader", "text": f"Just aped into {token}", "timestamp": "2025-06-13T10:23:00Z"},
            {"user": "@onchainalpha", "text": f"{token} volume spike on Arbitrum", "timestamp": "2025-06-13T09:58:00Z"}
        ],
        "trend": "rising"
    }
