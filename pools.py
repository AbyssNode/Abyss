# pools.py

from fastapi import APIRouter, Depends
from auth import verify_api_key

router = APIRouter()

@router.get("/pools", dependencies=[Depends(verify_api_key)])
def get_liquidity_pools():
    return [
        {
            "token": "TokenX",
            "dex": "Uniswap",
            "pair": "TokenX/ETH",
            "liquidity_usd": 210000
        },
        {
            "token": "DeepGem",
            "dex": "SushiSwap",
            "pair": "DeepGem/USDC",
            "liquidity_usd": 120000
        }
    ]
