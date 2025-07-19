# veil_detector.py

def detect_veil(tokens):
    """
    Identifies potentially cloaked tokens using low-noise/high-pattern tactics.
    """
    veiled = []
    for token in tokens:
        if token["tx_noise"] < 0.2 and token["pattern_score"] > 0.8:
            veiled.append(token["symbol"])
    return veiled
