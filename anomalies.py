# anomalies.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/anomalies")
def detect_anomalies():
    return {
        "anomalies": [
            {"token": "VaultFi", "type": "score spike", "change": "+14pts in 2h"},
            {"token": "DustX", "type": "volume surge", "change": "+340%"},
            {"token": "MoonDrain", "type": "price drop", "change": "-47%"}
        ]
    }
