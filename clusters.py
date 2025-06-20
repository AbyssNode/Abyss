# clusters.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/clusters")
def get_token_clusters():
    return {
        "clusters": [
            {
                "label": "Low cap + rising",
                "tokens": ["TokenX", "DeepGem", "PulseDrop"]
            },
            {
                "label": "High whale exposure",
                "tokens": ["SubAqua", "SilentMoon", "EchoNode"]
            }
        ],
        "generated_at": "2025-06-14T13:00:00Z"
    }
