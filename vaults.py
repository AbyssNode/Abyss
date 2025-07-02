# vaults.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/vaults")
def get_vault_analysis():
    return {
        "vault_tokens": [
            {
                "token": "SafeDrop",
                "vault_locked_usd": 870000,
                "lock_period_days": 180,
                "wallet_count": 4
            },
            {
                "token": "CoreStack",
                "vault_locked_usd": 430000,
                "lock_period_days": 90,
                "wallet_count": 2
            }
        ]
    }
