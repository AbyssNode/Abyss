# funding.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/funding")
def get_token_funding(token: str = Query(...)):
    return {
        "token": token,
        "presale_detected": True,
        "vc_wallets": [
            {"wallet": "0xABC...123", "label": "Seed Round", "tokens": 5_000_000},
            {"wallet": "0xDEF...456", "label": "Private Sale", "tokens": 2_500_000}
        ],
        "unlocked_tokens": "32%",
        "vesting_complete": "2025-12-01"
    }
