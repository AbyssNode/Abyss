# sandbox.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/sandbox")
def simulate_strategy(token: str = Query(...), strategy: str = Query(...)):
    return {
        "token": token,
        "strategy": strategy,
        "simulated_return": "+37.5%",
        "result": "Strategy would have outperformed holding",
        "period": "Last 14 days"
    }
