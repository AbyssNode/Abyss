# decode.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/decode")
def decode_contract_activity(address: str = Query(...)):
    return {
        "contract_address": address,
        "functions_detected": [
            "swapExactTokensForETH",
            "addLiquidityETH",
            "approve",
            "renounceOwnership"
        ],
        "flags": {
            "mintable": False,
            "trading_enabled": True,
            "anti_whale": True
        }
    }
