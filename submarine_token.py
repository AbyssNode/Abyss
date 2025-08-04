# submarine_token.py

def detect_submarine(tokens):
    """
    Flags tokens that have remained stable in low-volume markets, potentially setting up for stealth growth.
    """
    submarine = []
    for token in tokens:
        if token["volume"] < 50000 and token["price_change"] < 0.05:
            submarine.append(token["symbol"])
    return submarine
