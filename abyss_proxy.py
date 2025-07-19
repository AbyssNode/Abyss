# abyss_proxy.py

def simulate_query(query_type, token):
    """
    Returns a mock engine response for frontend previews or testing.
    """
    if query_type == "risk":
        return {"token": token, "risk_score": 0.73}
    elif query_type == "velocity":
        return {"token": token, "velocity_index": 1.4}
    return {"error": "unknown query type"}
