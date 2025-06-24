# liquidity_movement.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/liquidity/movement")
def get_lp_flows(token: str = Query(...)):
    return {
        "token": token,
        "last_24h": {
            "added_usd": 85000,
            "removed_usd": 42000,
            "net": "+43K"
        },
        "dex": "Uniswap",
        "pool_address": "0xPool...ABC"
    }
