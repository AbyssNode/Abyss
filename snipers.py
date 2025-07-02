# snipers.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/snipers")
def get_detected_snipers():
    return {
        "wallets_flagged": [
            {"wallet": "0xSn1p3r...123", "entry_delay_ms": 400, "profit_est_usd": 3200},
            {"wallet": "0xQuick...987", "entry_delay_ms": 620, "profit_est_usd": 2400}
        ],
        "tokens_affected": ["TokenX", "DeepGem"]
    }
