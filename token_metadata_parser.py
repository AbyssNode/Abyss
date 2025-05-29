# token_metadata_parser.py

def parse_metadata(raw_token):
    """
    Extracts and normalizes key token metadata.
    """
    return {
        'name': raw_token.get('name', 'Unknown'),
        'symbol': raw_token.get('symbol', '---'),
        'launch_date': raw_token.get('launch', 'N/A'),
        'verified': raw_token.get('verified', False)
    }
