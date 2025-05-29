# dex_registry.py

SUPPORTED_DEXES = [
    {"name": "Uniswap", "chain": "Ethereum"},
    {"name": "PancakeSwap", "chain": "BSC"},
    {"name": "TraderJoe", "chain": "Avalanche"},
    {"name": "SushiSwap", "chain": "Multichain"}
]

def get_supported_dexes():
    return SUPPORTED_DEXES
