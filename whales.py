# whales.py

from fastapi import APIRouter, Depends
from auth import verify_api_key

router = APIRouter()

@router.get("/whales", dependencies=[Depends(verify_api_key)])
def get_whale_activity():
    # Simulated whale movement data
    return [
        {
            "wallet": "0xABC123...xyz",
            "action": "buy",
            "token": "TokenX",
            "amount_usd": 120000
        },
        {
            "wallet": "0xDEF456...abc",
            "action": "sell",
            "token": "SubAqua",
            "amount_usd": 98000
        }
    ]
