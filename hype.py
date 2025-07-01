# hype.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/hype")
def detect_hype_signals():
    return {
        "hype_tokens": [
            {"token": "VoidRise", "discord_mentions": 188, "new wallets": 241},
            {"token": "ZenDrop", "volume_24h": "+390%", "trend_score": 91.4}
        ]
    }
