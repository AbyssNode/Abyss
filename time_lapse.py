# time_lapse.py

def track_time_lapse(token_data, period=30):
    """
    Tracks a token's price and volume changes over a specified period (in days).
    Returns token status based on the period’s data.
    """
    status = {}
    for token in token_data:
        price_change = (token["price"][-1] - token["price"][0]) / token["price"][0]
        volume_change = (token["volume"][-1] - token["volume"][0]) / token["volume"][0]
        
        status[token["symbol"]] = {
            "price_change": round(price_change, 2),
            "volume_change": round(volume_change, 2),
            "status": "surging" if price_change > 0.1 else "stable"
        }
    
    return status
