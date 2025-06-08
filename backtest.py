# backtest.py

from fastapi import APIRouter, Depends, Query
from auth import verify_api_key
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/backtest", dependencies=[Depends(verify_api_key)])
def run_backtest(
    token: str = Query(..., description="Token name or symbol to simulate"),
    days: int = Query(30, description="Number of past days to simulate")
):
    simulated_data = []
    current_score = random.uniform(80, 95)

    for i in range(days):
        day = (datetime.utcnow() - timedelta(days=i)).strftime("%Y-%m-%d")
        score = round(current_score + random.uniform(-2, 2), 2)
        price = round(1 + (score - 85) * 0.05, 2)  # fake price scaling logic
        simulated_data.append({
            "date": day,
            "score": score,
            "price_usd": price
        })

    simulated_data.reverse()
    return {
        "token": token,
        "days": days,
        "results": simulated_data
    }
