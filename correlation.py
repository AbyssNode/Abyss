# correlation.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/correlation")
def compare_token_correlation(
    token_a: str = Query(...),
    token_b: str = Query(...)
):
    return {
        "pair": f"{token_a} vs {token_b}",
        "correlation_score": 0.82,
        "trend": "Strong positive",
        "window_days": 30
    }
