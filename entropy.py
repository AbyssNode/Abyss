# entropy.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/entropy")
def get_entropy_score(token: str = Query(...)):
    return {
        "token": token,
        "entropy_score": 73.4,
        "description": "Measures unpredictability in volume, price, and score movement",
        "signal_strength": "medium"
    }
