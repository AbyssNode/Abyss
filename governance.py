# governance.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/governance")
def get_governance_data(token: str = Query(...)):
    return {
        "token": token,
        "active_proposals": [
            {
                "title": "Proposal #42 – Add staking rewards",
                "status": "voting",
                "votes_for": 321_000,
                "votes_against": 89_500
            }
        ],
        "snapshot": "https://snapshot.org/#/token.eth"
    }
