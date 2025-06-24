# tax_flags.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/tax-flags")
def get_token_tax_flags(token: str = Query(...)):
    return {
        "token": token,
        "buy_tax": "6%",
        "sell_tax": "12%",
        "dynamic_tax": True,
        "warning": "Sell tax over 10% — high-risk"
    }
