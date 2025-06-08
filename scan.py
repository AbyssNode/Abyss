# scan.py

from fastapi import APIRouter, Depends
from auth import verify_api_key

router = APIRouter()

@router.post("/scan", dependencies=[Depends(verify_api_key)])
def run_scan():
    # Simulated scan trigger (replace with actual function later)
    result = {
        "status": "Scan started",
        "tokens_discovered": [
            {"name": "TokenX", "score": 91},
            {"name": "DeepGem", "score": 87}
        ]
    }
    return result
