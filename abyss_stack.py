# abyss_stack.py

def stack_signals(token):
    """
    Combines multiple signal inputs to create a weighted conviction score.
    """
    volume = token.get("volume_spike", False)
    whale = token.get("whale_entry", False)
    anomaly = token.get("anomaly_flag", False)

    score = sum([
        3 if volume else 0,
        4 if whale else 0,
        5 if anomaly else 0
    ])
    
    return {
        "symbol": token["symbol"],
        "stack_score": score,
        "signal_combo": [k for k, v in token.items() if v is True]
    }
