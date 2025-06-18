# triggers.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/triggers")
def get_active_triggers():
    return {
        "active_triggers": [
            {"type": "whale_buy", "token": "SilentMoon", "amount_usd": 220000},
            {"type": "contract_change", "token": "VaultFi", "event": "RenounceOwnership()"}
        ]
    }
