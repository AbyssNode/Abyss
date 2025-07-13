# drift_monitor.py

def detect_drift(tokens):
    """
    Flags tokens with slow, consistent directional movement.
    Useful for detecting stealth accumulation or exit.
    """
    drifting = []
    for token in tokens:
        if abs(token["avg_daily_change"]) < 0.01 and token["directional_bias"] != 0:
            drifting.append(token["symbol"])
    return drifting
