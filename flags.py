# flags.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/flags")
def get_token_flags(token: str = Query(...)):
    return {
        "token": token,
        "flags": [
            "Liquidity not locked",
            "Unverified owner wallet",
            "High slippage detected"
        ],
        "risk_level": "medium"
    }
