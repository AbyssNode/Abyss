# watchlist.py

from fastapi import APIRouter, Depends, Query
from auth import verify_api_key

router = APIRouter()
watchlist = set()

@router.post("/watchlist/add", dependencies=[Depends(verify_api_key)])
def add_token(token: str = Query(...)):
    watchlist.add(token.upper())
    return {"added": token.upper(), "current_watchlist": list(watchlist)}

@router.get("/watchlist", dependencies=[Depends(verify_api_key)])
def get_watchlist():
    return {"watchlist": list(watchlist)}
