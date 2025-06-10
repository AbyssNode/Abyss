# sentiment.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/sentiment")
def get_token_sentiment(token: str = Query(...)):
    return {
        "token": token,
        "score": 72.4,
        "trend": "rising",
        "summary": "Increasing positive mentions on X and Telegram"
    }
