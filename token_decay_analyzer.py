# token_decay_analyzer.py

def analyze_token_decay(history):
    """
    Identifies tokens that are slowly losing volume, interest, or liquidity.
    """
    decaying = []
    for token in history:
        if token['avg_volume_7d'] < token['avg_volume_30d']:
            if token['liquidity_change'] < -0.05:
                decaying.append(token['symbol'])
    return decaying
