# liquidity_spike_detector.py

def detect_liquidity_spikes(tokens):
    """
    Flags tokens with abnormal liquidity increases.
    """
    flagged = []
    for token in tokens:
        if token['liquidity_now'] > token['liquidity_24h'] * 1.5:
            flagged.append(token['symbol'])
    return flagged
