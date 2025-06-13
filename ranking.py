# ranking.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/ranking")
def get_token_rankings():
    return {
        "top_tokens": [
            {"rank": 1, "token": "AbyssPrime", "score": 94.6},
            {"rank": 2, "token": "EchoNode", "score": 91.3},
            {"rank": 3, "token": "DeepGem", "score": 89.0}
        ]
    }
