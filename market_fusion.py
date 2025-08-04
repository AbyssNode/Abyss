# market_fusion.py

def merge_market_data(data_sources):
    """
    Merges market data from multiple sources, resolving conflicts by priority.
    Each data source is a dictionary: {"source": "uniswap", "data": {...}, "priority": 1}
    """
    merged_data = {}
    for source in data_sources:
        for token, token_data in source["data"].items():
            if token not in merged_data or source["priority"] > merged_data[token]["priority"]:
                merged_data[token] = {**token_data, "source": source["source"], "priority": source["priority"]}
    return merged_data
