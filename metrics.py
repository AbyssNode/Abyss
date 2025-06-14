# metrics.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
def get_system_metrics():
    return {
        "requests_served": 12942,
        "active_users": 47,
        "avg_scan_time_ms": 432,
        "memory_usage_mb": 187.5,
        "api_hit_distribution": {
            "/tokens": 5231,
            "/whales": 3092,
            "/signals": 2845
        }
    }
