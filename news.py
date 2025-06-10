# news.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/news")
def get_latest_news():
    return [
        {
            "title": "Microcap Surge: Hidden tokens outperform majors",
            "source": "DeFi Journal",
            "published": "2025-06-08"
        },
        {
            "title": "Whale shifts $2.3M into obscure alt",
            "source": "WhaleWatch",
            "published": "2025-06-07"
        }
    ]
