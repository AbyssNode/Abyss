# age.py

from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/age")
def get_token_age(token: str = Query(...)):
    return {
        "token": token,
        "contract_created": "2024-11-23",
        "age_days": 203,
        "block": 19420484
    }
