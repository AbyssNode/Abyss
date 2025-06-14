# compare.py

from fastapi import APIRouter, Query
from typing import List

router = APIRouter()

@router.get("/compare")
def compare_tokens(tokens: List[str] = Query(...)):
    return {
        "tokens": tokens,
        "comparison": [
            {"token": "TokenX", "score": 91, "holders": 143, "liq_usd": 125000},
            {"token": "DeepGem", "score": 88, "holders": 76, "liq_usd": 98000}
        ]
    }
