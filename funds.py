# funds.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/funds")
def get_wallet_funds(wallet: str = Query(...)):
    return {
        "wallet": wallet,
        "holdings": [
            {"token": "DeepGem", "amount": 12500, "usd_value": 5400},
            {"token": "TokenX", "amount": 4800, "usd_value": 3100}
        ],
        "total_value_usd": 8500
    }
