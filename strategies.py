# strategies.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/strategies")
def get_token_strategies(token: str = Query(...)):
    return {
        "token": token,
        "strategies": [
            {
                "name": "Whale Bounce",
                "entry": "After whale buy > $50K",
                "exit": "Price +15% or 48h max hold",
                "success_rate": "72%"
            },
            {
                "name": "Volume Pulse",
                "entry": "Volume surge > 300%",
                "exit": "Score decline by 10+ pts",
                "success_rate": "64%"
            }
        ]
    }
