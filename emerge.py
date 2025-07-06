# emerge.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/emerge")
def get_emerging_tokens():
    return {
        "emerging": [
            {"token": "GhostPad", "new_wallets_24h": 721, "volume_change": "+312%"},
            {"token": "BlurNova", "score_gain": "+11 pts", "score_now": 86.3}
        ]
    }
