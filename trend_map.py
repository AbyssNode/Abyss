# trend_map.py

def build_trend_clusters(tokens):
    """
    Groups tokens that are showing similar trend directions.
    Uses simple correlation based on price movement.
    """
    clusters = {'up': [], 'down': [], 'flat': []}
    for token in tokens:
        if token['trend'] > 0.05:
            clusters['up'].append(token['symbol'])
        elif token['trend'] < -0.05:
            clusters['down'].append(token['symbol'])
        else:
            clusters['flat'].append(token['symbol'])
    return clusters
