# liquidity_heatmap.py

def generate_heatmap(token_data):
    """
    Creates a heatmap-ready matrix of liquidity distribution across tokens.
    """
    matrix = []
    for token in token_data:
        matrix.append({
            'symbol': token['symbol'],
            'liquidity': token['liquidity'],
            'chain': token.get('chain', 'unknown')
        })
    return matrix
