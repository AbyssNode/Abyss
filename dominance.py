# dominance.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/dominance")
def get_token_dominance(token: str = Query(...)):
    return {
        "token": token,
        "dominance_score": 68.4,
        "pool_control_percent": 42.7,
        "volume_dominance_percent": 35.2,
        "summary": "Dominance reflects LP control + trading activity share"
    }
