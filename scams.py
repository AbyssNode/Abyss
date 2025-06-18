# scams.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/scams")
def get_flagged_tokens():
    return {
        "flagged": [
            {"token": "RugToken", "reason": "Trading disabled, liquidity pulled"},
            {"token": "DrainFi", "reason": "Anti-sell function active"},
        ],
        "last_updated": "2025-06-13T08:00:00Z"
    }
