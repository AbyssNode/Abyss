# whale_profiles.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/whale-profile")
def get_whale_profile(wallet: str = Query(...)):
    return {
        "wallet": wallet,
        "type": "builder whale",
        "total_txns": 148,
        "buy_ratio": "73%",
        "avg_hold_time": "4.2 days",
        "notable_moves": [
            {"token": "TokenX", "action": "buy", "amount_usd": 120000},
            {"token": "SubAqua", "action": "exit", "amount_usd": 80000}
        ]
    }
