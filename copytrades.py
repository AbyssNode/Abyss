# copytrades.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/copytrades")
def get_copytrade_sim(wallet: str = Query(...)):
    return {
        "wallet": wallet,
        "strategy": "Mirror all buys over $20K",
        "simulated_return": "+51.2%",
        "duration": "Last 14 days",
        "top_token": "DeepGem"
    }
