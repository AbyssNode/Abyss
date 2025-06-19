# alpha.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/alpha")
def get_today_alpha():
    return {
        "token": "SilentMoon",
        "score": 93.2,
        "confidence": "very high",
        "reason": "Whale activity + volume + sentiment alignment",
        "as_of": "2025-06-14T12:00:00Z"
    }
