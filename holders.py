# holders.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/holders")
def get_holder_distribution(token: str = Query(...)):
    return {
        "token": token,
        "total_holders": 1234,
        "top_10_percent_hold": "68%",
        "contract_ownership": "renounced",
        "wallet_concentration": {
            "top_1": "28%",
            "top_5": "51%",
            "top_10": "68%"
        }
    }
