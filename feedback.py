# feedback.py

from fastapi import APIRouter, Depends, Form
from auth import verify_api_key
import datetime

router = APIRouter()

@router.post("/feedback", dependencies=[Depends(verify_api_key)])
def submit_feedback(token: str = Form(...), rating: int = Form(...), notes: str = Form("")):
    timestamp = datetime.datetime.utcnow().isoformat()
    return {
        "message": "Feedback received",
        "data": {
            "token": token,
            "rating": rating,
            "notes": notes,
            "timestamp": timestamp
        }
    }
