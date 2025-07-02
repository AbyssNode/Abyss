# floorwatch.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/floorwatch")
def watch_new_floors():
    return {
        "potential_floors": [
            {"token": "VoidRise", "price": 0.0039, "detected_at": "2025-06-14T14:55:00Z"},
            {"token": "DriftFi", "price": 0.0087, "detected_at": "2025-06-14T15:12:00Z"}
        ]
    }
