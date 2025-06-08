# config_api.py

from fastapi import APIRouter, Depends
from auth import verify_api_key
from config import settings

router = APIRouter()

@router.get("/config", dependencies=[Depends(verify_api_key)])
def get_config():
    return {
        "MIN_SCORE_THRESHOLD": settings.MIN_SCORE_THRESHOLD,
        "WHALE_MIN_TX": settings.WHALE_MIN_TX,
        "ENABLE_DEEP_SCAN": settings.ENABLE_DEEP_SCAN,
        "ENABLE_WHALE_TRACKER": settings.ENABLE_WHale_TRACKER,
        "LOG_LEVEL": settings.LOG_LEVEL
    }
