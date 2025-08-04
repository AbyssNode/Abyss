# surge_predictor.py

def predict_surge(history, window=3, threshold=0.12):
    """
    history: list of dicts ordered oldest->newest
             [{"price":..., "volume":...}, ...]
    Returns True if recent momentum suggests an impending surge.
    """
    if len(history) < window + 1:
        return False

    deltas = []
    for i in range(-window, -1):
        prev = history[i - 1]
        curr = history[i]
        p_delta = (curr["price"] - prev["price"]) / max(prev["price"], 1e-9)
        v_delta = (curr["volume"] - prev["volume"]) / max(prev["volume"], 1e-9)
        deltas.append(0.7 * p_delta + 0.3 * v_delta)

    momentum = sum(deltas) / len(deltas)
    return momentum > threshold
