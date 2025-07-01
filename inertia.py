# inertia.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/inertia")
def get_inertia(token: str = Query(...)):
    return {
        "token": token,
        "inertia_score": 84.2,
        "definition": "Momentum vs decay ratio over past 48h",
        "interpretation": "Holding strong upward movement with little fallback"
    }
