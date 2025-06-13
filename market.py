# market.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/market")
def get_market_movers():
    return {
        "gainers": [
            {"token": "PulseFi", "change_24h": "+44%"},
            {"token": "VoidLink", "change_24h": "+38%"}
        ],
        "losers": [
            {"token": "NovaSwap", "change_24h": "-27%"},
            {"token": "DustX", "change_24h": "-19%"}
        ]
    }
