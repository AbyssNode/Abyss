# models.py

from fastapi import APIRouter, Depends
from auth import verify_api_key

router = APIRouter()

current_model = "abyss-v1-lite"

@router.get("/models", dependencies=[Depends(verify_api_key)])
def get_model_info():
    return {
        "current_model": current_model,
        "available_models": ["abyss-v1-lite", "abyss-v1-heavy", "abyss-v2-exp"]
    }

@router.post("/models/select", dependencies=[Depends(verify_api_key)])
def switch_model(name: str):
    global current_model
    if name in ["abyss-v1-lite", "abyss-v1-heavy", "abyss-v2-exp"]:
        current_model = name
        return {"status": "model switched", "new_model": current_model}
    return {"error": "invalid model name"}
