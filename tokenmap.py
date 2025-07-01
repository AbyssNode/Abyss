# tokenmap.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/tokenmap")
def get_token_map():
    return {
        "ecosystems": [
            {"root_token": "TokenX", "linked": ["DeepGem", "GemRouter", "NodeFi"]},
            {"root_token": "SubAqua", "linked": ["AquaSwap", "HydroLock"]}
        ]
    }
