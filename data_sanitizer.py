# data_sanitizer.py

def sanitize_token_data(raw_data):
    """
    Ensures input data has required fields and safe values.
    Removes tokens with missing or invalid metrics.
    """
    clean = []
    for token in raw_data:
        if 'symbol' in token and 'price' in token and token['price'] >= 0:
            clean.append(token)
    return clean
