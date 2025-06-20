# influencers.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/influencers")
def get_influencer_impact(token: str = Query(...)):
    return {
        "token": token,
        "trending_accounts": [
            {"handle": "@entrydefi", "impact_score": 9.2},
            {"handle": "@zero_gas_bot", "impact_score": 8.1}
        ],
        "mentions_last_24h": 37
    }
