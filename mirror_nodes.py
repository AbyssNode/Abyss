# mirror_nodes.py

def find_mirror_nodes(wallet_data):
    """
    Detects wallets that repeatedly mimic transactions of larger whales.
    """
    mirrors = []
    for wallet in wallet_data:
        if wallet.get("mimic_rate", 0) > 0.75 and wallet["tx_volume"] < 10000:
            mirrors.append(wallet["address"])
    return mirrors
