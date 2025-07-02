# velocity.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/velocity")
def get_velocity(token: str = Query(...)):
    return {
        "token": token,
        "velocity_score": 77.6,
        "change_24h": "+8.2 pts",
        "volatility_ratio": 1.31,
        "description": "Rate of score acceleration vs price volatility"
    }
