# momentum_score.py

def calculate_momentum(token):
    """
    Returns a score based on recent price change and trade volume surge.
    """
    price_change = token.get('price_change_24h', 0)
    volume_change = token.get('volume_change_24h', 0)

    score = (price_change * 100) + (volume_change / 1000)
    return round(score, 2)
