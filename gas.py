# gas.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/gas")
def get_gas_prices():
    return {
        "ethereum": {"gwei": 28, "usd": 0.52},
        "arbitrum": {"gwei": 0.45, "usd": 0.01},
        "base": {"gwei": 1.2, "usd": 0.03},
        "polygon": {"gwei": 43, "usd": 0.12}
    }
}
