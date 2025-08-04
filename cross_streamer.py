# cross_streamer.py

def stream_data_across_chains(chains, token_symbol):
    """
    Streams token data across multiple chains and consolidates information into one view.
    chains: List of chain APIs like [{'chain': 'eth', 'url': '...'}, ...]
    """
    token_data = {}
    for chain in chains:
        response = requests.get(chain["url"] + f"/api/v1/token/{token_symbol}")
        if response.status_code == 200:
            token_data[chain["chain"]] = response.json()
    return token_data
