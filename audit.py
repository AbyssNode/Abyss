# audit.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/audit")
def run_security_audit(token: str = Query(...)):
    return {
        "token": token,
        "issues_found": [
            "Liquidity not locked",
            "No max transaction limit",
            "Verified but renounced"
        ],
        "score": 78
    }
