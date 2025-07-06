# threats.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/threats")
def get_token_threat_list():
    return {
        "tokens_with_active_risks": [
            {"token": "DrainFi", "risk": "Sell tax spiked to 25%"},
            {"token": "StealthX", "risk": "Ownership reclaimed by dev wallet"}
        ],
        "last_checked": "2025-06-14T17:00:00Z"
    }
