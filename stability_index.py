# stability_index.py

def calculate_stability(token):
    """
    Generates a basic score to represent market stability.
    Factors: liquidity, volume, price fluctuation.
    """
    liquidity = token.get('liquidity', 0)
    volume = token.get('volume', 0)
    price_volatility = token.get('volatility', 0.0)

    score = (liquidity + volume) / (1 + price_volatility * 1000)
    return round(score, 2)
