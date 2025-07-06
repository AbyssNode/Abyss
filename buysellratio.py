# buysellratio.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/buysellratio")
def get_buy_sell_ratio(token: str = Query(...)):
    return {
        "token": token,
        "buys": 128,
        "sells": 91,
        "ratio": 1.41,
        "trend": "buy-side pressure"
    }
