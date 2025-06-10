# network.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/network")
def get_network_info():
    return {
        "networks_supported": ["Ethereum", "Arbitrum", "Solana"],
        "default_network": "Ethereum",
        "gas_tracking_enabled": True
    }
